import subprocess

GPD_PATH = "/home/aidan/ManiSkill/grasp/gpd/build/generate_grasps"
CFG_PATH = "/home/aidan/ManiSkill/grasp/gpd/cfg/eigen_params.cfg"

def convert_pcd(pc):


	pcd_text = ""
	pcd_text += "VERSION .7\n"
	pcd_text += "FIELDS x y z rgb\n"
	pcd_text += "SIZE 4 4 4 4\n"
	pcd_text += "TYPE F F F I\n"
	pcd_text += "COUNT 1 1 1 1\n"
	pcd_text += "WIDTH 4467\n"
	pcd_text += "HEIGHT 1\n"
	pcd_text += "POINTS 4467\n"
	pcd_text += "DATA ascii\n"

	for pc_point_index in range(pc.shape[0]):
		pcd_text += str(float(pc[pc_point_index, 0]))+" " +\
					str(float(pc[pc_point_index, 1]))+" " +\
					str(float(pc[pc_point_index, 2]))+" 0\n"

	return pcd_text

def write_pc(pc, pcd_filename="/home/aidan/ManiSkill/temp/obj.pcd"):

	""" Input: Num_points x 3 dimensional numpy array containing the x, y, z coordinates of the points in the pointcloud
		Effects: Writes the pointcloud to a pcd file specified by the pcd_filename
	"""

	# Write pc to a pcd file
	pcd_text = convert_pcd(pc)
	with open(pcd_filename, "w") as pcd_file:
		pcd_file.write(pcd_text)
	pcd_file.close()

def generate_grasps(pc, pc_color):

	# Call gpd
	subprocess.run(GPD_PATH+" "+CFG_PATH+" "+pcd_filename, shell=True, check=True)

	# Read the results
	grasp_filename = "./temp/grasps.txt"

	grasp_file = open(grasp_filename, 'r')
	count = 0
	grasps = []
	while True:
		count += 1
		# Get next line from file
		line = file1.readline()

		items = line.split("\n")[0].split(",")
		grasps.append([float(i) for i in items])
	 
		# if line is empty
		# end of file is reached
		if not line:
			break
		print("Line{}: {}".format(count, line.strip()))
	 
	grasp_file.close()

	return grasps