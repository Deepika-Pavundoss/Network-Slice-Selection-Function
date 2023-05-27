import mysql.connector
# Define network slice classes
class NetworkSlice:
    def __init__(self, name, lw_latency,up_latency, lw_bandwidth,up_bandwidth,jitter):
        self.name = name
        self.lw_latency = lw_latency
        self.up_latency= up_latency
        self.lw_bandwidth = lw_bandwidth
        self.up_bandwidth = up_bandwidth
        self.jitter=jitter



# Define network slice configurations
S1_A = NetworkSlice("Slice Type A", 20,50, 1,100000, "low")
S1_B = NetworkSlice("Slice Type B", 10000,-1, 0,0, "variable")
S1_C = NetworkSlice("Slice Type C", 0,1,1,10, "very low")
S1_D = NetworkSlice("Slice Type D", 10,100,50,50000, "low")
S1_E = NetworkSlice("Slice Type E", 20,50, 100,1000 ,"high") 
S1_F = NetworkSlice("Slice Type F", 10000,-1,0,0 ,"variable")
S1_G = NetworkSlice("Slice Type G", 0,1,1,10 ,"very low")
err_object= NetworkSlice("Error. No service found.", 0,1,1,10 ,"very low")


# #connecting to sql and getting responses to test 
# conn = mysql.connector.connect(user='root', password='password',
#                                host='mysql-container', database='nssf',port=3306)

# uid = int(input("Enter your user id:"))
# app = input("Enter the desired application:")

# cursor = conn.cursor()
# stmt = "select * from slicerepo where app = %(app)s"
# cursor.execute(stmt, {'app': app})
# res = cursor.fetchall()
# requestedNSSAI = res[0][0]
# cursor.close()
# conn.close()

# Define function to select network slice based on latency and bandwidth requirements
def select_network_slice(latency, bandwidth,jitter):
    if latency <= S1_A.up_latency and latency >= S1_A.lw_latency and bandwidth >= S1_A.lw_bandwidth and bandwidth <= S1_A.up_bandwidth and jitter==S1_A.jitter:
        return S1_A
    elif latency <= S1_B.up_latency and latency >= S1_B.lw_latency and bandwidth >= S1_B.lw_bandwidth and bandwidth <= S1_B.up_bandwidth and jitter==S1_B.jitter:
        return S1_B
    elif latency <= S1_C.up_latency and latency >= S1_C.lw_latency and bandwidth >= S1_C.lw_bandwidth and bandwidth <= S1_C.up_bandwidth and jitter==S1_C.jitter:
        return S1_C
    elif latency <= S1_D.up_latency and latency >= S1_D.lw_latency and bandwidth >= S1_D.lw_bandwidth and bandwidth <= S1_D.up_bandwidth and jitter==S1_D.jitter:
        return S1_D
    elif latency <= S1_E.up_latency and latency >= S1_E.lw_latency and bandwidth >= S1_E.lw_bandwidth and bandwidth <= S1_E.up_bandwidth and jitter==S1_E.jitter:
        return S1_E
    elif latency <= S1_F.up_latency and latency >= S1_F.lw_latency and bandwidth >= S1_F.lw_bandwidth and bandwidth <= S1_F.up_bandwidth and jitter==S1_F.jitter:
        return S1_F
    elif latency <= S1_G.up_latency and latency >= S1_G.lw_latency and bandwidth >= S1_G.lw_bandwidth and bandwidth <= S1_G.up_bandwidth and jitter==S1_G.jitter:
        return S1_G
    else:
        return err_object
    
    
# Define function to test network slice selection
def test_network_slice_selection():
    # Define a list of test cases
    test_cases = [
        {"input": (30, 5000,"low"), "output": S1_A},
        {"input": (1, 5, "very low"), "output": S1_C},
        {"input": (20, 5000,"low"), "output": S1_A},
        {"input": (40, 700, "high"), "output": S1_E},
        {"input": (30, 500, "low"), "output": S1_A},
        {"input": (4000, 0, "variable"), "output": err_object},
        {"input": (0, 7, "very low"), "output": S1_C},
    ]
    
    
    # Loop over the test cases and check the output
    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["output"]
        actual_output = select_network_slice(input_data[0],input_data[1],input_data[2])
        # print(res[0][7])
        # print(res[0][6])
        # print(res[0][9])
        # print(actual_output.bandwidth_threshold)
        # Check if the output matches the expected value
        if actual_output == expected_output:
            print(f"Test case passed: input={input_data}, output={actual_output.name}")

        else:
            print(f"Test case failed: input={input_data}, expected_output={expected_output.name}, actual_output={actual_output.name}")

# Run the test function
test_network_slice_selection()