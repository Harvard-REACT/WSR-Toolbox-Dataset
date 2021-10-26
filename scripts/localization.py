import numpy as np
import json
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def ray_localize(start_points:np.array, end_points:np.array):
    Si = end_points - start_points
    ni = Si / np.tile(np.sqrt((np.sum(Si**2,axis = 1))).reshape((-1,1)),(1,3))
    nx = ni[:,0]
    ny = ni[:,1]
    nz = ni[:,2]
    SXX = np.sum(nx**2-1)
    SYY = np.sum(ny**2-1)
    SZZ = np.sum(nz**2-1)
    SXY = np.sum(nx*ny)
    SXZ = np.sum(nx*nz)
    SYZ = np.sum(ny*nz)
    s = np.array([[SXX, SXY, SXZ],[SXY ,SYY,SYZ],[SXZ,SYZ, SZZ]])
    CX = np.sum(start_points[:,0]*(nx**2-1)+start_points[:,1]*(nx*ny)+start_points[:,2]*(nx*nz))
    CY = np.sum(start_points[:,0]*(nx*ny)+start_points[:,1]*(ny**2-1)+start_points[:,2]*(ny*nz))
    CZ = np.sum(start_points[:,0]*(nx*nz)+start_points[:,1]*(ny*nz)+start_points[:,2]*(nz**2-1))
    C = np.array([CX,CY,CZ])
    P_intersect = np.linalg.solve(s,C)
    return P_intersect

# print(ray_localize(np.array([[1,2,3],[1,4,5]]),np.array([[2,6,10],[5,6,8]])))
def read_json(set_n:str, if_LOS:bool, traj_type:str):
    fn = '../Dataset/2D-Displacement_output_files/offboard/'
    if if_LOS:
        fn = fn + "LOS"
    else:
        fn = fn + "NLOS"   
    fn = fn + '_Set_{}_using_{}_displacement.json'.format(set_n, traj_type)    
    num_rob = 3
    if "NLOS" in fn and "Set_A" in fn:
        print('NLOS Set A')
        num_rob = 3
    if "NLOS" in fn and "Set_B" in fn:
        #NLOS set B
        num_rob = 3
        print("NLOS Set B")

    if "NLOS" in fn and "Set_C" in fn:
    #NLOS set C
        print('NLOS Set C')
        num_rob = 1
    if "NLOS" not in fn and "Set_A" in fn:
        #LOS set A
        print('LOS Set A')
    if "NLOS" not in fn and "Set_B" in fn:
    #LOS set B
        print("LOS Set B")
    with open(fn) as f:
        data = json.load(f)
    res_dict_list = []
    exp_count = 1
    while(1):
        try:
            res_dict = {}
            # aoa = [0 for i in range(num_rob)]
            res_dict['aoa'] = [0 for i in range(num_rob)]
            # aoa_close = [0 for i in range(num_rob)]
            res_dict['aoa_closest'] =  [0 for i in range(num_rob)]
            # aoa_error = [0 for i in range(num_rob)]
            res_dict['aoa_error'] = [0 for i in range(num_rob)]
            # aoa_closest_error = [0 for i in range(num_rob)]
            res_dict['aoa_closest_error'] = [0 for i in range(num_rob)]
            # variance = [0 for i in range(num_rob)]
            res_dict['variance'] = [0 for i in range(num_rob)]
            # variance_closest = [0 for i in range(num_rob)]
            res_dict['variance_closest'] = [0 for i in range(num_rob)]
            res_dict['tx_pos'] = [0 for i in range(num_rob)]
            for i in range(num_rob):
                exp = data[str(exp_count)][i]
                tx_idx = int(exp["a_INFO_Transmitting_robot"]["Name"][-1])-2
                tx_idx = tx_idx if num_rob > 1 else 0
                res_dict['aoa'][tx_idx] = round(exp['d_INFO_AOA_profile']['Top_N_peaks']["1"]["estimated_azimuth"],2)/180*math.pi
                # res_dict['aoa_closest'][tx_idx] = round(exp['d_INFO_AOA_profile']['Phi(deg)'],2)
                res_dict['aoa_error'][tx_idx] = round(exp['d_INFO_AOA_profile']['Top_N_peaks']["1"]['azimuth_error'],2)
                # res_dict['aoa_closest_error'][tx_idx] = round(exp['d_Info_AOA_Closest']['Phi_Error(deg)'],2)
                res_dict['rx_idx'] = int(exp["b_INFO_Receiving_robot"]['id'])
                res_dict['rx_x'] = round(float(exp["b_INFO_Receiving_robot"]["groundtruth_start_position"]["x"]),2)
                res_dict['rx_y'] = round(float(exp["b_INFO_Receiving_robot"]["groundtruth_start_position"]["y"]),2)
                res_dict['variance'][tx_idx] = exp['d_INFO_AOA_profile']['Profile_variance']
                res_dict['variance_closest']  = 0
                res_dict['tx_pos'][tx_idx] = (exp['a_INFO_Transmitting_robot']['groundtruth_position']['x'],
                exp['a_INFO_Transmitting_robot']['groundtruth_position']['y'],0)
            # if num_rob == 3:
            #     res_mat[exp_count-1,:] = np.array([aoa[0],aoa_close[0],aoa[1],aoa_close[1],aoa[2],aoa_close[2],x1,y1,x2,y2,x3,y3,rx_x, rx_y,loc,
            #     aoa_error[0], aoa_error[1],aoa_error[2],aoa_closest_error[0],aoa_closest_error[1],aoa_closest_error[2],
            #     variance[0],variance[1],variance[2],variance_closest[0],variance_closest[1],variance_closest[2]])
            # elif num_rob == 2:
            #     res_mat[exp_count-1,:] = np.array([aoa[0],aoa_close[0],aoa[1],aoa_close[1],x1,y1,x2,y2,rx_x, rx_y,loc,
            #     aoa_error[0], aoa_error[1],aoa_closest_error[0],aoa_closest_error[1],
            #     variance[0],variance[1],variance_closest[0],variance_closest[1]])
            res_dict_list.append(res_dict)
        except KeyError:
            print(f"Finished processing, {exp_count} procssed in total")
            break
        exp_count = exp_count + 1
    return res_dict_list
def run(if_LOS:bool, traj_type:str,if_convex_hull:bool):
    threshold = 0.9
    #Load data by LOS/NLOS and traj type
    localize_data = []
    if if_LOS:
        localize_data.append(read_json('A',if_LOS,traj_type))
        localize_data.append(read_json('B',if_LOS,traj_type))
        trial_idx = [0, 0]
    elif not if_LOS and if_convex_hull:
        localize_data.append(read_json('A',if_LOS,traj_type))
        localize_data.append(read_json('B',if_LOS,traj_type))
        localize_data.append(read_json('C',if_LOS,traj_type))
        trial_idx = [0, 0,0]
    elif not if_LOS and not if_convex_hull:
        localize_data.append(read_json('A',if_LOS,traj_type))
        localize_data.append(read_json('B',if_LOS,traj_type))
        trial_idx = [0, 0]
    error_list_allloc = []
    error_closest_list_allloc = []
    for loc in range(10):
        error_list_loc = []
        error_closest_list_loc = []  
        curr_loc_data = [list() for i in range(len(trial_idx))]
        for set_n in range(len(trial_idx)):
            for i in range(len(localize_data[set_n])):
                if localize_data[set_n][i]['rx_idx'] == loc+1:
                    curr_loc_data[set_n].append(localize_data[set_n][i])

        for i in range(min([len(curr_loc_data[i]) for i in range(len(curr_loc_data))])):
            aoa_list = []
            aoa_closest_list = []
            tx_pos = []
            var_list = []
            for set_n in range(len(curr_loc_data)):
                aoa_list.extend(curr_loc_data[set_n][i]['aoa'])
                aoa_closest_list.extend(curr_loc_data[set_n][i]['aoa_closest'])
                tx_pos.extend(curr_loc_data[set_n][i]['tx_pos'])
                var_list.extend(curr_loc_data[set_n][i]['variance'])
                rx_pos = (curr_loc_data[set_n][i]['rx_x'],curr_loc_data[set_n][i]['rx_y'],0)
            idx_var_below_threshold = [i  for i in range(len(var_list)) if var_list[i] < threshold]
            if len(idx_var_below_threshold) <= 5:
                continue
            start_points = np.zeros((len(tx_pos),3))
            end_points = np.zeros((len(tx_pos),3))

            for tx_idx in range(len(tx_pos)):
                start_points[tx_idx] = np.array([tx_pos[tx_idx][0], tx_pos[tx_idx][1],0])
                end_points[tx_idx] = np.array([0, math.tan(aoa_list[tx_idx])*(-tx_pos[tx_idx][0])+tx_pos[tx_idx][1],0])
            localized_rx = ray_localize(start_points[idx_var_below_threshold], end_points[idx_var_below_threshold])
            eu_error = math.sqrt((localized_rx[0]-rx_pos[0])**2+(localized_rx[1]-rx_pos[1])**2)
            error_list_loc.append(eu_error)
        error_list_allloc.extend(error_list_loc)
        # print(error_list_allloc)
        #increament set-wise pointer
    return error_list_allloc

def plot_cdf(error):    
    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12
    plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
# ​    raw_data =  pd.read_csv("../data/Dataset-1-REACT_LAB_FINAL_first_pose_localization/Convex_non_convex_hull_final_plot/6rays_rejection_camera_2d_var_res.csv", delimiter=',')
    # raw_data2 = pd.read_csv("../data/Dataset-1-REACT_LAB_FINAL_first_pose_localization/Convex_non_convex_hull_final_plot/7rays_rejection_camera_2d_var_res.csv", delimiter=',')
    # raw_data3 = pd.read_csv("../data/Dataset-1-REACT_LAB_FINAL_first_pose_localization/Convex_non_convex_hull_final_plot/6rays_los_rejection_camera_2d_var_res.csv", delimiter=',')
    raw_data = {"loc_error":error[1]}
    raw_data2 = {"loc_error":error[0]}
    raw_data3 = {"loc_error":error[2]}
    # raw_data = {"loc_error":error}
#     print("Using Rejection- est, Non-convex hull")
#     print("Using top peak, mean error = ", raw_data["loc_error"].mean())
#     print("Using top peak, median error = ",raw_data["loc_error"].median())
#     print("Using closest peak, mean error = ", raw_data["closest_loc_error"].mean())
#     print("Using closest peak,  median error = ", raw_data["closest_loc_error"].median())
# # ​
# # ​
#     print("Using Rejection- est, Convex hull")
#     print("Using top peak, mean error = ", raw_data2["loc_error"].mean())
#     print("Using top peak, median error = ",raw_data2["loc_error"].median())
#     print("Using closest peak, mean error = ", raw_data2["closest_loc_error"].mean())
#     print("Using closest peak,  median error = ", raw_data2["closest_loc_error"].median())
    '''
    Using top peak
    '''
    localization_error = []
    peak_type=[]

    for val in raw_data["loc_error"]:
        localization_error.append(val)
        peak_type.append("NLOS-non-convex-hull-est")

    for val in raw_data2["loc_error"]:
        localization_error.append(val)
        peak_type.append("NLOS-convex-hull-est")
# ​
    for val in raw_data3["loc_error"]:
        localization_error.append(val)
        peak_type.append("LOS")
# ​
    my_data = pd.DataFrame()
    my_data["localization_error"] = localization_error
    my_data["peak_type"] = peak_type

    my_data["localization_error"] = abs(my_data["localization_error"])

    sns.ecdfplot(data=my_data, 
                x="localization_error",
                hue="peak_type")

    plt.xlabel("Error(meters)")
    plt.ylabel("Density")
    # plt.xlim([-20, 180])
    plt.title('Localization Error')
    plt.show()
    '''
    Using closest peak
    '''
#     localization_error = []
#     peak_type=[]
# ​
#     for val in raw_data["closest_loc_error"].tolist():
#         localization_error.append(val)
#         peak_type.append("convex-hull-est")
# ​
# ​
#     for val in raw_data2["closest_loc_error"].tolist():
#         localization_error.append(val)
#         peak_type.append("non-convex-hull-est")
    
#     my_data = pd.DataFrame()
#     my_data["localization_error"] = localization_error
#     my_data["peak_type"] = peak_type
# ​
# ​
#     my_data["localization_error"] = abs(my_data["localization_error"])

    # sns.ecdfplot(data=my_data, 
#                 x="localization_error",
#                 hue="peak_type")
# ​
#     plt.xlabel("Localization error (meters)")
#     plt.ylabel("Density")
#     # plt.xlim([-20, 180])
#     plt.title('Localization Error using closest peak 8 TX')
    # plt.show()


if __name__=='__main__':
    #Groundtuth
    if_LOS = False
    if_convex_hull = True
    error1 = run(if_LOS,'groundtruth',if_convex_hull)
    print(len(error1))
    if_convex_hull = False
    error2 = run(if_LOS,'groundtruth',if_convex_hull)
    print(len(error2))
    if_LOS = True
    error3 = run(if_LOS,'groundtruth',if_convex_hull)
    print("Len", len(error3))
    plot_cdf([error1,error2,error3])
    plot_cdf([error3,error3,error3])

    #T265 trajectory
    if_LOS = False
    if_convex_hull = True
    error1 = run(if_LOS,'t265',if_convex_hull)
    print(len(error1))
    if_convex_hull = False
    error2 = run(if_LOS,'t265',if_convex_hull)
    print(len(error2))
    if_LOS = True
    error3 = run(if_LOS,'t265',if_convex_hull)
    print(len(error3))
    plot_cdf([error1,error2,error3])


    #Offboard parallelized
    # if_convex_hull = False
    # if_LOS = True
    # error1 = run(if_LOS,'groundtruth',if_convex_hull)
    # error2 = run(if_LOS,'offboard',if_convex_hull)
    # plot_cdf([error1,error2,error2])