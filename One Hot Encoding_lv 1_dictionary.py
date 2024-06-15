"""
Objective: one hot encoding
Principle: 
- Input:
    ID, Trait
    1, ["A"]
    2, ["B"]
    3, ["C"]
    4, ["A"]
- Output:
    ID, Trait
    1, [1, 0, 0]
    2, [0, 1, 0]
    3, [0, 0, 1]
    4, [1, 0, 0]
"""

# Case study 1: No Pandas, just dictionary
df_in = {1: ["A"],
         2: ["B"],
         3: ["C"],
         4: ["A"]}

print("Input dictionary:\n", df_in)

# create a function that return one hot encoding according to the letter
# create a position dict, then replace 1 at word's location
position = {"A": 0,
            "B": 1,
            "C": 2}
    
# transform input dataframe
def one_hot_encoding(df_in):
    df_out = df_in.copy()
    
    for k in df_out.keys():
        zeros = [0, 0, 0]  # zeros frame
        value = df_out[k][0]  # get value for position dict
        zeros[position[value]] = 1  # replace 0 at location by 1
        df_out[k] = zeros
    return df_out

print("Encoded:\n", one_hot_encoding(df_in))