from extract import extract_data
from transform import transform_data
from load import load_data_to_db
from validate import validate_data

def main():
    file_a = 'order_region_a(in).csv'
    file_b = 'order_region_b(in).csv'

    # Extract data
    df_a = extract_data(file_a)
    df_b = extract_data(file_b)

    if df_a is not None and df_b is not None:

        transformed_data = transform_data(df_a, df_b)
        print(transform_data)

        db_path = "sales_data.db"
        load_data_to_db(transformed_data, db_path)


        validation_results = validate_data()
        print("Validation Results:")
        print(validation_results)
    else:
        print("Error in extracting data. Process aborted.")

if __name__ == "__main__":
    main()
