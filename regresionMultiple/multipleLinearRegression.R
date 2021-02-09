#----regresion lineal multiple---
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
               data=training_set)#asi se remplasa (.) para las demas var(~ significa en funcion de..)
#predesimos los resultados con el conjunto de testing
y_pred=predict(regression,newdata=testing_set)
# se construye un modelo optimo con la eliminacion hacia atras

# ----Iniciamos con todas la variables ----
regression= lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data=dataSet)
#dado los valores de significancia de las columnas se elimina la de State(los cuales fueron Adm,State)
regression= lm(formula=Profit ~ R.D.Spend + Marketing.Spend,
               data=dataSet)

#Probamos con el nuevo modelo
 y_pred = predict(regression,newdata = testing_set)
 