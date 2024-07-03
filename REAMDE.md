# INSURANCE PREMIUM ESTIMATE AND CROSS-SALE PREDICTION

# Goal: 

* The goal is to determine whether policyholders from the past year would also be interested in purchasing vehicle insurance offered by the company.
* Identify the Health Insurance policyholder who will be interested in  purchasing vehicle insurance based on demographic and policy-related features. This will provide actionable insights for the company to tailor its communication strategy and optimize business operations.

# Background:
* An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee. 
* In case of an unfortunate accident involving the insured vehicle, the insurance provider compensates the customer (referred to as the “sum assured”).
* People belonging to rural India do not have credit score and it is difficult to do a direct assessment.

# Feature Description:

* id:	                    Unique ID for the customer
* Gender:	                Gender of the customer
* Age:	                    Age of the customer
* Driving_License:	        0 (Customer does not have DL) 1 (Customer already has DL)
* Region_Code:	            Unique code for the region of the customer
* Previously_Insured:	    1 (Customer already has Vehicle Insurance), 0 (Customer doesn't have Vehicle Insurance)
* Vehicle_Age:              Age of the Vehicle
* Vehicle_Damage:	        1 (Customer got his/her vehicle damaged in the past.) 0 (Customer didn't get his/her vehicle damaged in the past.)
* Annual_Premium:	        The amount customer needs to pay as premium in the year
* Policy_Sales_Channel:	    Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
* Vintage:	                Number of Days, Customer has been associated with the company
* Response:	                1 (Customer is interested), 0 (Customer is not interested)

 # Solution Approach
 Steps Followed for Building Machine Learning  Model:
 
Step 1: Loading the dataset from the  prompt
			-The user is asked to select the input file
			-The user is allowed to load only  CSV file format as per current scenario

Step 2: Handling anomalies
			- Hist plot and desriptive statistics is used for handling annomalies in the annual premium.
      
Step 3: Converting categorical features into numeric:
			- One-hot encoding is performed on categorical features:Gender, Vehicle_Damage, and Vehicle_Age.
      
Step 4: Tested multiple models to identify best model for premium estimate
			- used decision tree, and ensemble technique to determine best model for estimation
      
Step 5: Added estimated premium to original data 
		    - Model for predicting customer vehicle insurance interest, and determined accuracy, precision, f1-score, and auc-roc score are calculated

# Code Execution Steps:
* python notebook and scripts files are present: eda and modeling.ipynb and script.py.
* 


# Note 
* train.csv: I have used this dataset for the use case.

