# NOVA Cybersecurity
# AI-Powered Threat Detection and Risk Assessment System
#
# Current version: Rule-based prototype.
# Machine learning will be added in a future version.

print("=" * 50)
print("              NOVA CYBERSECURITY")
print("=" * 50)
print("AI-Powered Threat Detection and Risk Assessment System")
print("")

# Get login information
device = input("Is this a new device? (yes/no): ").strip().lower()
location = input("Is this an unusual location? (yes/no): ").strip().lower()

while True:
    try:
        failed_attempts = int(input("How many failed login attempts? "))

        if failed_attempts < 0:
            print("Please enter a number 0 or greater.")
            continue

        break

    except ValueError:
        print("Please enter a valid whole number.")

print("")
print("Information received successfully!")
print("")

# Calculate risk score
risk_score = 0

if device == "yes":
    risk_score += 30

if location == "yes":
    risk_score += 40

if failed_attempts >= 5:
    risk_score += 30

# Keep risk score between 0 and 100
risk_score = min(risk_score, 100)

# Determine risk level
if risk_score <= 30:
    risk_level = "LOW"

elif risk_score <= 70:
    risk_level = "MEDIUM"

else:
    risk_level = "HIGH"

# Determine alert level
if risk_score >= 80:
    alert_level = "CRITICAL"

elif risk_score >= 50:
    alert_level = "WARNING"

else:
    alert_level = "SAFE"

# Determine security action
if risk_score >= 80:
    action = "LOGIN BLOCKED"
    reason = "High security risk detected."

elif risk_score >= 50:
    action = "VERIFICATION REQUIRED"
    reason = "Additional identity verification is required."

else:
    action = "LOGIN ALLOWED"
    reason = "Login appears safe."

# Display NOVA security report
print("=" * 50)
print("              NOVA SECURITY REPORT")
print("=" * 50)

print("NOVA Risk Score:", risk_score, "/ 100")
print("Risk Level:", risk_level)
print("Alert Level:", alert_level)
print("Security Action:", action)
print("Reason:", reason)

# Suspicious login detection
if risk_score >= 70:
    print("WARNING: Suspicious login detected!")

else:
    print("Login appears normal.")

print("=" * 50)
print("NOVA analysis completed.")
print("=" * 50)
