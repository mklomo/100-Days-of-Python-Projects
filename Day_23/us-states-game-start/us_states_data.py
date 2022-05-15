import pandas as pd


us_states_df = pd.read_csv("50_states.csv")


# Keep a list of all the states for reference
us_states_names_list = us_states_df.state.to_list()


def xy_coord(state_name):
    x_coord_list = us_states_df[us_states_df.state == state_name].x.to_list()
    y_coord_list = us_states_df[us_states_df.state == state_name].y.to_list()
    xy = tuple(x_coord_list + y_coord_list)
    return xy


coord = xy_coord(state_name="Colorado")
print(coord)


