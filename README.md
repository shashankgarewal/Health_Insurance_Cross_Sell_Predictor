# INSURANCE CROSS-SALE PREDICTION

This readme is still in making..

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

# Steps to contribute to the project
* Make a clone

# Code Execution Steps:
* python notebook and scripts files are present at respective folders.
* 


# Note 
* train.csv: I have used this dataset for preprocessing performed during EDA and stored the preprocessed data in [artificats](/artifacts/data.csv).
* Dataset can be found in [kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).
