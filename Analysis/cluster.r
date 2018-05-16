library(ClustOfVar)
library(cluster)

# Choose columns for clustering
data <- abilities[, c(3:13)]
data <- positions[, c(3:17)]


# Cluster variables
# Find data clusters
tree <- hclustvar(data)

# Plot cluster dendrogram
png(file="position_cluster.png", res=128, width=3000, height=2000)
plot(tree)
dev.off()

# Estimate number of clusters
stab <- stability(tree, B=64)
plot(stab)


# Cluster respondants
# Get distances for columns
d <- dist(data, method = "euclidian")

# K-means cluster
kfit <- kmeans(d, 4)
clusplot(as.matrix(d), kfit$cluster, color=T, shade=T, labels=2, lines=0)


