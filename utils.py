import numpy as np
import pickle
import json
import config

class CreditModel():
    def __init__(self,Total_TL_opened_L6M, Tot_TL_closed_L6M, pct_tl_open_L6M, pct_tl_closed_L6M, pct_closed_tl, Tot_TL_closed_L12M, 
                 pct_tl_open_L12M, pct_tl_closed_L12M, Tot_Missed_Pmnt, Age_Oldest_TL, Age_Newest_TL, time_since_recent_payment, 
                 num_times_delinquent, max_recent_level_of_deliq, num_times_60p_dpd, num_std, num_std_6mts, num_sub, num_sub_6mts, 
                 num_sub_12mts, num_dbt, num_dbt_6mts, num_dbt_12mts, num_lss, recent_level_of_deliq, tot_enq, CC_enq, CC_enq_L6m, 
                 CC_enq_L12m, PL_enq, PL_enq_L6m, time_since_recent_enq, enq_L12m, enq_L3m, NETMONTHLYINCOME, Time_With_Curr_Empr, 
                 pct_opened_TLs_L6m_of_L12m, CC_Flag, PL_Flag, pct_PL_enq_L6m_of_ever, HL_Flag, GL_Flag, MARITALSTATUS, EDUCATION, 
                 GENDER, last_prod_enq2, first_prod_enq2):
        
        self.Total_TL_opened_L6M = Total_TL_opened_L6M
        self.Tot_TL_closed_L6M = Tot_TL_closed_L6M
        self.pct_tl_open_L6M = pct_tl_open_L6M
        self.pct_tl_closed_L6M = pct_tl_closed_L6M
        self.pct_closed_tl = pct_closed_tl
        self.Tot_TL_closed_L12M = Tot_TL_closed_L12M
        self.pct_tl_open_L12M = pct_tl_open_L12M
        self.pct_tl_closed_L12M = pct_tl_closed_L12M
        self.Tot_Missed_Pmnt = Tot_Missed_Pmnt
        self.Age_Oldest_TL = Age_Oldest_TL
        self.Age_Newest_TL = Age_Newest_TL
        self.time_since_recent_payment = time_since_recent_payment
        self.num_times_delinquent = num_times_delinquent
        self.max_recent_level_of_deliq = max_recent_level_of_deliq
        self.num_times_60p_dpd = num_times_60p_dpd
        self.num_std = num_std
        self.num_std_6mts = num_std_6mts
        self.num_sub = num_sub
        self.num_sub_6mts = num_sub_6mts
        self.num_sub_12mts = num_sub_12mts
        self.num_dbt = num_dbt
        self.num_dbt_6mts = num_dbt_6mts
        self.num_dbt_12mts = num_dbt_12mts
        self.num_lss = num_lss
        self.recent_level_of_deliq = recent_level_of_deliq
        self.tot_enq = tot_enq
        self.CC_enq = CC_enq
        self.CC_enq_L6m = CC_enq_L6m
        self.CC_enq_L12m = CC_enq_L12m
        self.PL_enq = PL_enq
        self.PL_enq_L6m = PL_enq_L6m
        self.time_since_recent_enq = time_since_recent_enq
        self.enq_L12m = enq_L12m
        self.enq_L3m = enq_L3m
        self.NETMONTHLYINCOME = NETMONTHLYINCOME
        self.Time_With_Curr_Empr = Time_With_Curr_Empr
        self.pct_opened_TLs_L6m_of_L12m = pct_opened_TLs_L6m_of_L12m
        self.CC_Flag = CC_Flag
        self.PL_Flag = PL_Flag
        self.pct_PL_enq_L6m_of_ever = pct_PL_enq_L6m_of_ever
        self.HL_Flag = HL_Flag
        self.GL_Flag = GL_Flag
        self.MARITALSTATUS = MARITALSTATUS
        self.EDUCATION = EDUCATION
        self.GENDER = GENDER
        self.last_prod_enq2 = last_prod_enq2
        self.first_prod_enq2 = first_prod_enq2

    def load_model(self):
        with open(config.model_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.pipe_path ,'rb') as file:
            self.pipe=pickle.load(file)    

        with open(config.json_path,'r') as file:
            self.json_data=json.load(file)   

    def get_credit_TL(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
    
    # Filled in the test_array with the corresponding values from the JSON data
        test_array[0] = self.json_data['pct_tl_open_L6M']
        test_array[1] = self.json_data['pct_tl_closed_L6M']
        test_array[2] = self.json_data['Tot_TL_closed_L12M']
        test_array[3] = self.json_data['pct_tl_closed_L12M']
        test_array[4] = self.json_data['Tot_Missed_Pmnt']
        test_array[5] = self.json_data['Age_Oldest_TL']
        test_array[6] = self.json_data['Age_Newest_TL']
        test_array[7] = self.json_data['time_since_recent_payment']
        test_array[8] = self.json_data['max_recent_level_of_deliq']
        test_array[9] = self.json_data['num_times_60p_dpd']
        test_array[10] = self.json_data['num_std_12mts']
        test_array[11] = self.json_data['num_sub']
        test_array[12] = self.json_data['num_sub_6mts']
        test_array[13] = self.json_data['num_sub_12mts']
        test_array[14] = self.json_data['num_dbt']
        test_array[15] = self.json_data['num_dbt_12mts']
        test_array[16] = self.json_data['num_lss']
        test_array[17] = self.json_data['recent_level_of_deliq']
        test_array[18] = self.json_data['CC_enq_L12m']
        test_array[19] = self.json_data['PL_enq_L12m']
        test_array[20] = self.json_data['time_since_recent_enq']
        test_array[21] = self.json_data['enq_L3m']
        test_array[22] = self.json_data['NETMONTHLYINCOME']
        test_array[23] = self.json_data['Time_With_Curr_Empr']
        test_array[24] = self.json_data['CC_Flag']
        test_array[25] = self.json_data['PL_Flag']
        test_array[26] = self.json_data['pct_PL_enq_L6m_of_ever']
        test_array[27] = self.json_data['HL_Flag']
        test_array[28] = self.json_data['GL_Flag']
    
    # Handle categorical fields like gender, marital status, education
        gender_index = self.json_data['columns'].index('GENDER')
        test_array[gender_index] = self.json_data['GENDER'][self.gender]
    
        marital_status_index = self.json_data['columns'].index('MARITALSTATUS')
        test_array[marital_status_index] = self.json_data['MARITALSTATUS'][self.marital_status]
    
        education_index = self.json_data['columns'].index('EDUCATION')
        test_array[education_index] = self.json_data['EDUCATION'][self.education]
    
        # Predict charges based on the model
        predict_class = self.model.predict([test_array])
        return predict_class


