#importamos el dataSet
dataSet=read.csv("50_Startups.csv")
#manejo de datos categoricos
dataSet$State=factor(dataSet$State,
                     levels = c("New York","California","Florida"),
                     labels = c(1,2,3))
#divimos el conjunto de entrenamiento y test
set.seed(123)
split=sample.split(dataSet$Profit,SplitRatio = 0.8)

training_set=subset(dataSet,split==TRUE)
testing_set=subset(dataSet,split==FALSE)
#ajustamos el modelo con el conjunto de entrenamiento
regression= lm(formula=Profit ~.,
               data=training_set)
backwardElimination<- function(x,sl) {
  nVars = length(x)
  for (i in c(1:nVars)){
    regressor = lm(formula = Profit ~., data = x)
    #maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    maxVar = max(coef(summary(regressor))[c(2:nVars),"Pr(>|t|)"])
    if(maxVar > sl){
      #j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      j = which(coef(summary(regressor))[c(2:nVars),"Pr(>|t|)"] == maxVar)
      x = x[,-j]
    }
    nVars = nVars -1 
  }
  return(summary(regressor))
} 
SL = 0.05 
dataSet = dataSet[,c(1,2,3,4,5)]
backwardElimination(training_set,SL)


