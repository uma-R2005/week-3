class CertificateEligibleMixin:
    def is_eligible_for_certificate(self):
        return self.passed and self.score >= 70 and self.hours_spent >= 5

class CourseCompletion(CertificateEligibleMixin):
    def __init__(self, name, score, hours_spent, passed):
        self.name = name
        self.score = score
        self.hours_spent = hours_spent
        self.passed = passed

    def get_summary(self):
        status = "Eligible" if self.is_eligible_for_certificate() else "Not eligible"
        return f"{self.name} | Score: {self.score} | Hours: {self.hours_spent} | Passed: {self.passed} → {status} for certificate"

# -------- User Input Example --------
name = input("Enter your name: ")
score = float(input("Enter your final score (0-100): "))
hours = float(input("How many hours did you spend on the course?: "))
passed = input("Did you pass the course? (yes/no): ").strip().lower() == "yes"

completion = CourseCompletion(name, score, hours, passed)
print("\n" + completion.get_summary())
