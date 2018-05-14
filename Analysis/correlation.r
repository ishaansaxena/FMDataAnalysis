library(corrplot)

# Significance test function from http://www.sthda.com/english/wiki/visualize-correlation-matrix-using-correlogram
# mat : is a matrix of data
# ... : further arguments to pass to the native R cor.test function
cor.mtest <- function(mat, ...) {
  mat <- as.matrix(mat)
  n <- ncol(mat)
  p.mat<- matrix(NA, n, n)
  diag(p.mat) <- 0
  for (i in 1:(n - 1)) {
    for (j in (i + 1):n) {
      tmp <- cor.test(mat[, i], mat[, j], ...)
      p.mat[i, j] <- p.mat[j, i] <- tmp$p.value
    }
  }
  colnames(p.mat) <- rownames(p.mat) <- colnames(mat)
  p.mat
}

# Plotting correlation in abilities
# Choosing data
data <- abilities[, c(3:64)]

# Significance values
p.mat <- cor.mtest(data)

# Calculate correlation values
M <- cor(data)

# Plot graph of ability correlations
png(file="Plots/abilities.png", res=72, width=6000, height=6000)
corrplot(M, method = "color", type="full", order="hclust", 
         addCoef.col = "black", number.digits = 2,
         # p.mat = p.mat, sig.level = 0.01, 
         tl.cex = 3, number.cex = 3, cl.pos = 'b', cl.cex = 3, 
         addrect = 10, rect.lwd = 5,
         diag = TRUE)
dev.off()

# Plotting corrlation in positional abilities
# Choosing data
data <- positions[, c(3:17)]

# Significance values
p.mat <- cor.mtest(data)

# Calculate correlation values
M <- cor(data)

# Plot graph of ability correlations
png(file="positions.png", res=128, width=2000, height=2000)
corrplot(M, method = "color", type="full", order="hclust", 
         addCoef.col = "black", number.digits = 2,
         p.mat = p.mat, sig.level = 0.01, #insig = "blank",
         #tl.cex = 3, number.cex = 3, cl.pos = 'b', cl.cex = 3, 
         addrect = 10, rect.lwd = 2,
         diag = TRUE)
dev.off()

