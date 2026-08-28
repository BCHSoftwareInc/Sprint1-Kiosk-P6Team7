# QA Test Execution Matrix - Sprint 1
* **QA Tester:** @FatGavin
* **Client Deliverable:** Console Interactive Kiosk

| Test ID | Target Input Field | Test Input Description | Expected Output | Actual Behavior | Status (Pass/Fail) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Full Name | Standard text (`"Jane Doe"`) | Formatted correctly in ASCII box |Formatted correctly in ASCII| Pass |
| TC-02 | Department/Role | Blank input (`""`) | Handles gracefully without crash |Handled without crash |Pass |
| TC-03 | Email / Contact | Valid string (`"test@bch.org"`) | Stored & printed accurately | | |
| TC-04 | Badge Tier | Lowercase text (`"vip"`) | Clean output on badge |Displayed correctly on badge |Pass |
| TC-05 | Badge Tier | Uppercase text (`"VIP"`) | Clean output on badge |Displayed correctly on badge |Pass |
| TC-06 | Badge Tier | Mixed case text (`"ViP"`) | Clean output on badge |Displayed correctly on badge |Pass |
| TC-07 | Badge Tier | Special characters (`"@#$%"`) | Handles gracefully without crash |Handled and displayed as imputed on badge |Pass |
| TC-08 | Email / Contact | Invalid email format (`"test@bch"`) | Error message displayed|Handled without crash |(Failed) |