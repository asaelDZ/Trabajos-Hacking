# SECURITY.md

## Q0: Why is an unauthenticated incident tracker a security problem?

An unauthenticated incident tracker is a security problem because anyone could access sensitive cybersecurity incident information without permission. In a real system, this could expose vulnerabilities, attack details, affected systems, and internal security reports.

## Q1: User model vs UserProfile — why OneToOneField?

Django's built-in User model stores basic authentication data such as username, email, password, and permissions. The UserProfile model extends that user with extra information such as role, bio, and joined date. A OneToOneField is used because each user should have only one profile, keeping Django's original User model clean and secure.

## Q2: Purpose of ?next= and open redirect risk

The `?next=` parameter tells Django where to redirect a user after login. For example, if a user tries to access `/incidents/`, Django sends them to login and then returns them to the original page. If Django did not validate the next URL, an attacker could use an open redirect attack to send users to a malicious website after login.

## Q3: Authentication vs Authorization

Authentication verifies who the user is, for example logging in with username and password. Authorization verifies what the user is allowed to do. In this lab, all users must log in to access incidents, but only Admin users can edit or delete incidents. If authentication is implemented without authorization, any logged-in user could perform dangerous actions.

## Q4: commit=False and mass assignment risk

`commit=False` is used to create the object without saving it immediately to the database. This allows the system to automatically assign `reported_by = request.user` before saving. If users were allowed to submit the `reported_by` field manually, they could impersonate another user. This relates to mass assignment or improper authorization.

## Q5: Why template hiding is NOT enough security

Hiding Edit and Delete buttons in the template is not enough because users can still manually type the URL in the browser, such as `/incidents/1/delete/`. Security must be enforced in the view with role checks. The attack that bypasses template-level hiding is direct URL access or forced browsing.

## Q6: Brute-force attacks and django-axes mitigation

A brute-force attack is when an attacker tries many username and password combinations until one works. `django-axes` helps mitigate this by blocking or limiting repeated failed login attempts. If `AXES_FAILURE_LIMIT` is too low, legitimate users may be locked out by mistake. Another protection method is using multi-factor authentication or CAPTCHA.
