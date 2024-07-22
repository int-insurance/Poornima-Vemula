#%%
import configparser

 
def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()
 
    # Read the configuration file
    config.read(r'D:\Code_Optimization\balic\Config\config.ini')
 
    # Access values from the configuration file
    date_value_path = config.get('Path', 'date_value_path')
    dsr_file_path = config.get('Path', 'dsr_file_path')
    lead_file_path = config.get('Path', 'lead_file_path')
    days_list_path = config.get('Path', 'days_list_path')
    manpower_file_path = config.get('Path', 'manpower_file_path')
    target_file_path = config.get('Path', 'target_file_path')
    slab_grid_file_path = config.get('Path', 'slab_grid_file_path')
    save_output_file_path = config.get('Path', 'save_output_file_path')

    hostname = config.get('SFTP', 'hostname')
    username_indusnet = config.get('SFTP', 'username_indusnet')
    password_indusnet = config.get('SFTP', 'password_indusnet')
    username_salesadmin = config.get('SFTP', 'username_salesadmin')
    password_salesadmin = config.get('SFTP', 'password_salesadmin')

 
    # Return a dictionary with the retrieved values
    config_values = {
        'date_value_path': date_value_path,
        'dsr_file_path': dsr_file_path,
        'lead_file_path': lead_file_path,
        'days_list_path': days_list_path,
        'manpower_file_path': manpower_file_path,
        'target_file_path': target_file_path,
        'slab_grid_file_path': slab_grid_file_path,
        'save_output_file_path': save_output_file_path,

        'hostname': hostname,
        'username_indusnet': username_indusnet,
        'password_indusnet': password_indusnet,
        'username_salesadmin': username_salesadmin,
        'password_salesadmin': password_salesadmin

    }

    return config_values

# %%
