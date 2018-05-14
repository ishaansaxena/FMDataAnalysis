# Test UID
uid <- 7458500
uidk <- 67030171

# Range definitions
low = 15
high = 20

# Choosing data
data <- abilities

# Get all abilities of a player with certain value
getAbilitiesInRange <- function(uid, low, high) {
  data <- abilities
  df <- data[which(data$UID == uid), ]
  print(paste0("Player Name: ", df$Name))
  cols <- names(df)[which(df >= low & df <= high, arr.ind = T)[, "col"]]
  cols
}
cols <- getAbilitiesInRange(uid, low, high)

# Get all players with abilities in a certain range
getPlayersByAbilitiesInRange <- function(cols, low, high) {
  df <- abilities
  for (i in 1:length(cols)) {
    df <- df[which(df[cols[i]] >= low & df[cols[i]] <= high), ]
  }
  df  
}
df <- getPlayersByAbilitiesInRange(cols, low, high)

# Get all players with similar abilities to a player
getSimilarPlayers <- function(uid, range) {
  df <- data[which(data$UID == uid), c(14:45, 47, 48, 50, 51)] # Exclude footedness, GK Stats, Hidden Stats
  low <- df - range
  high <- df + range
  cols <- names(df)[which(df >= 0 & df <= 20, arr.ind = T)[, "col"]]
  df <- abilities
  for (i in 1:length(cols)) {
    df <- df[which(df[cols[i]] >= as.integer(low[i]) & df[cols[i]] <= as.integer(high[i])), ]
  }
  df
}
getSimilarGoalkeepers <- function(uid, range) {
  df <- data[which(data$UID == uid), 3:13] # Only GK Stats
  low <- df - range
  high <- df + range
  cols <- names(df)[which(df >= 0 & df <= 20, arr.ind = T)[, "col"]]
  df <- abilities
  for (i in 1:length(cols)) {
    df <- df[which(df[cols[i]] >= as.integer(low[i]) & df[cols[i]] <= as.integer(high[i])), ]
  }
  df
}
getSimilarPlayers(55063369, 4)[, 1:2]
getSimilarGoalkeepers(uidk, 3)[, 1:2]
