import glob
import os
import pandas as pd

def clean_and_merge():
    csv_files = glob.glob("*.csv")
    master_list = []
    
    # Define standard target schema names
    standard_columns = {
        'Sector': 'Sector', 'AREA': 'Area', 'Area': 'Area',
        'Sex': 'Sex', 'Age Group': 'Age_Group', 'AgeGroup': 'Age_Group',
        'Month of Commencement': 'Commencement_Date', 'MonthOfCommencement': 'Commencement_Date', 'Month of commencement': 'Commencement_Date',
        'Treatment Duration Days': 'Treatment_Days', 'TreatmentDays': 'Treatment_Days',
        'Principal Drug Of Concern': 'Drug_Code', 'PrincipalDrugOfConcern': 'Drug_Code', 'Principal Drug of Concern': 'Drug_Code',
        'Main Treatment Type': 'Treatment_Type_Code', 'MainTreatmentType': 'Treatment_Type_Code'
    }

    print("Beginning structural normalization...")
    
    for file in csv_files:
        if file == "merged_australian_treatment_data.csv":
            continue # Avoid processing old output
            
        df = pd.read_csv(file)
        
        # Rename columns using our standard map dictionary
        df = df.rename(columns=standard_columns)
        
        # Keep only the essential columns we mapped for our analytical dashboard
        keep_cols = ['Sector', 'Area', 'Sex', 'Age_Group', 'Commencement_Date', 'Treatment_Days', 'Drug_Code', 'Treatment_Type_Code']
        df = df[[col for col in keep_cols if col in df.columns]]
        
        # Standardize the messy dates into a uniform format
        df['Commencement_Date'] = pd.to_datetime(df['Commencement_Date'], errors='coerce')
        
        master_list.append(df)
        print(f"Successfully aligned and processed: {file} ({len(df)} rows)")

    # Combine all records 
    master_df = pd.concat(master_list, ignore_index=True)
    
    # --- DECODING THE CLINICAL CODES ---
    # Python dictionary mapping standard codes to clinical names
    drug_map = {7101: 'Nicotine', 1202: 'Alcohol', 3903: 'Amphetamines', 2499: 'Cannabis'}
    treatment_map = {1: 'Counselling', 2: 'Withdrawal/Detox', 6: 'Assessment Only', 7: 'Rehabilitation'}
    sex_map = {1: 'Male', 2: 'Female'}
    
    master_df['Substance'] = master_df['Drug_Code'].map(drug_map).fillna('Other/Unstated Substance')
    master_df['Treatment_Type'] = master_df['Treatment_Type_Code'].map(treatment_map).fillna('Other Treatment')
    master_df['Gender'] = master_df['Sex'].map(sex_map).fillna('Unknown')
    
    # Drop raw code columns to keep the file light for Tableau
    master_df = master_df.drop(columns=['Drug_Code', 'Treatment_Type_Code', 'Sex'])
    
    output_name = "merged_australian_treatment_data.csv"
    master_df.to_csv(output_name, index=False)
    print(f"\nETL Pipeline Completed! Combined Master Sheet saved as: {output_name}")
    print(f"Total Rows Compiled for Tableau: {len(master_df)}")

if __name__ == "__main__":
    clean_and_merge()