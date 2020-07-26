from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        "create_medical_record": True,
    }


class Staff(AbstractUserRole):
    available_permissions = {
        "edit_patient_file": True,
    }
