import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PersonalDataForm = ({ personalData, onSuccess }) => {
    const [formData, setFormData] = useState({
        surname: '',
        first_name: '',
        middle_name: '',
        date_of_birth: '',
        place_of_birth: '',
        sex: '',
        civil_status: '',
        height: '',
        weight: '',
        blood_type: '',
        gsis_id_no: '',
        pagibig_id_no: '',
        philhealth_no: '',
        sss_no: '',
        tin_no: '',
        agency_employee_no: '',
        citizenship: '',
        residential_address: '',
        residential_zip_code: '',
        residential_telephone_no: '',
        permanent_address: '',
        permanent_zip_code: '',
        permanent_telephone_no: '',
        email_address: '',
        cell_phone_no: '',
        agency_no: ''
    });

    useEffect(() => {
        if (personalData) {
            setFormData({
                surname: personalData.surname,
                first_name: personalData.first_name,
                middle_name: personalData.middle_name || '',
                date_of_birth: personalData.date_of_birth,
                place_of_birth: personalData.place_of_birth,
                sex: personalData.sex,
                civil_status: personalData.civil_status,
                height: personalData.height,
                weight: personalData.weight,
                blood_type: personalData.blood_type,
                gsis_id_no: personalData.gsis_id_no,
                pagibig_id_no: personalData.pagibig_id_no,
                philhealth_no: personalData.philhealth_no,
                sss_no: personalData.sss_no,
                tin_no: personalData.tin_no,
                agency_employee_no: personalData.agency_employee_no,
                citizenship: personalData.citizenship,
                residential_address: personalData.residential_address,
                residential_zip_code: personalData.residential_zip_code,
                residential_telephone_no: personalData.residential_telephone_no || '',
                permanent_address: personalData.permanent_address,
                permanent_zip_code: personalData.permanent_zip_code,
                permanent_telephone_no: personalData.permanent_telephone_no || '',
                email_address: personalData.email_address,
                cell_phone_no: personalData.cell_phone_no,
                agency_no: personalData.agency_no
            });
        }
    }, [personalData]);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            if (personalData) {
                await axios.put(`http://localhost:8000/api/personaldata/${personalData.id}/`, formData);
            } else {
                await axios.post('http://localhost:8000/api/personaldata/', formData);
            }
            onSuccess();
        } catch (error) {
            console.error('There was an error submitting the form!', error);
        }
    };

    return (
        <div>
            <h1>Personal Data</h1>
            <form onSubmit={handleSubmit}>
                {Object.keys(formData).map((key) => (
                    <div key={key}>
                        <label>{key.replace(/_/g, ' ')}:</label>
                        <input
                            type='text'
                            name={key}
                            value={formData[key]}
                            onChange={handleChange}
                        />
                    </div>
                ))}
                <button type='submit'>Submit</button>
            </form>
        </div>
    );
};

export default PersonalDataForm;
