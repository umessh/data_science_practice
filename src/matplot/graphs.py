from matplotlib import pyplot as plt 

# x = [90, 91, 92, 93, 94]
# y = [10, 8 ,19, 8, 15]

# plt.plot(x, y, color="blue", linestyle="solid")

# plt.title("Dummy graph")
# plt.ylabel("Y-axis")
# plt.show()


# test_data = ['Test1','Test2','Test3']
# test_results = [1, 5, 10]
# xs = [i for i,_ in enumerate(test_results)]
# plt.bar(xs, test_results)

# plt.ylabel("Test results")
# plt.title("Dummy Bar chart")

# plt.xticks([i+0.5 for i,_ in enumerate(test_data)], test_data)

# plt.show()


friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends,minutes)
for friend, minutes, label in zip(friends, minutes, labels):

	plt.annotate(label, xy = (friend, minutes), xytext=(-5,5), textcoords='offset points')
plt.show()