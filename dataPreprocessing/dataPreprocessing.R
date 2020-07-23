#Aqui los inidices inician en 1
#importamos dataset
dataset=read.csv("Data.csv")
#tartamiento de datos faltantes
dataset$Age=ifelse(is.na(dataset$Age),
                   ave(dataset$Age, FUN = function(x) mean(x,na.rm=TRUE))
                   ,dataset$Age)
dataset$Salary=ifelse(is.na(dataset$Salary),
                   ave(dataset$Salary, FUN = function(x) mean(x,na.rm=TRUE))
                   ,dataset$Salary)



