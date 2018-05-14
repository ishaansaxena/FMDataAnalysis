library(readr)

# Import FM Dataset 
dataset <- read_csv("~/Envelope/Work/Data Science/Football Manager/dataset.csv")
abilities <- dataset[, c(1, 2, 12:73)]
positions <- dataset[, c(1, 2, 75:89)]


M <- data.matrix(abilities[, 3:66])
clust <- hclust(M)
clust
plot(clust)

