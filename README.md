# g-play-console-report-to-s3-python
 
# For Google authorization and integration witht the code, Please follow steps below
# Download reports using a client library and service account
Step 1: Create a service account

    Open Google Developers Console.
    If you already have a project, use the drop-down to select a project. If you don't have a project listed or want to create a new one, click Create project.
    Select the Menu icon Menu icon > Permissions > Service accounts > Create service account.
    Follow the on-screen instructions and select Create.
    Copy the email address listed.
        Example: accountName@project.iam.gserviceaccount.com

 
Step 2: Add the service account on Play Console

    Open Play Console.
    Select Settings Settings > User accounts & rights > Invite new user.
    Paste or type the email address associated with your service account.
    Based on the types of reports needed, select permissions. 
        Tip: Read the Add developer account users and manage permissions article to understand the different access levels users have and the rights that different permissions grant them.
    Click Add user. Your service account will be added to your account.
    
    
Step 3: Replace private_key.json with your private_key.json
    
    Download json file of your service account. (The one you created in step 1)
    Copy text from the downloaded file and paste it into private_key.json file available in project root directory.


 # Google cloud storage bucket details
 You can copy your Google Cloud Storage URI by following below steps:
  Sign in to your google play console
  Expand download reports section from the menu on the left (make sure you are not inside the app)
  Click your desired report section and your find button "Copy cloud storage URI"
  Your Cloud Storage URI begins with pubsite_prod_rev (e.g., pubsite_prod_rev_01234567890987654321).
  
  For files/paths inside bucket, please see "Commands and file formats for detailed reports" section by clicking this link https://support.google.com/googleplay/android-developer/answer/6135870
