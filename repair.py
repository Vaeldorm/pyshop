class Customer:
    def __init__(
        self, first_name, last_name, current_jobs=[], current_balance=0, tenure=0
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.current_jobs = current_jobs
        self.current_balance = current_balance
        self.tenure = tenure  # +1 on payment made for a completed repair

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Current Balance: {self.current_balance}, Tenure: {self.tenure}"


class Device:
    def __init__(self, type, brand, model_number, serial_number):
        self.type = type  # ex: Laptop, PC
        self.brand = brand
        self.model_number = model_number
        self.serial_number = serial_number

    def __str__(self):
        return f"{self.type}: {self.brand} {self.model_number} \n Serial Number: {self.serial_number}"


class Job:
    def __init__(
        self,
        customer,
        device,
        status,
        service_description,
        price=0,
        callback="Not needed at this time",
        service_updates=[],
    ):
        self.customer = customer
        self.device = device
        self.status = status
        self.service_description = service_description
        self.price = price
        self.callback = callback
        self.service_updates = service_updates  # List of strings provided as discoveries are made during work, as-needed

    def __str__(self):
        return f"""
                {self.device}, {self.service_description}\n
                for\n
                {self.customer}\n
                \n
                {self.status}, Contact Needed: {self.callback}\n
                Updates:\n
                {self.service_updates}
                """


def no_interface_test():
    customer = Customer("Gabby", "Hernandez")
    device = Device("Laptop", "Acer", 123456, 78910)
    job = Job(
        customer,
        device,
        status="Assessment",
        service_description="Diagnose power and repair",
    )

    return (customer, device, job)


for instance in no_interface_test():  # Test with hardcoded classes
    print(instance)
