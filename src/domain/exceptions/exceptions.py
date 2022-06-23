class FailOnRegister(Exception):
    ...

class NoRecordsFound(Exception):
    msg = "Contact not found with this id"
