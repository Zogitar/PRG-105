# Amount of each ingredient required per serving size:
clew = 1.25/16
cs = 1.5/16
ccf = 1/16
tct = 1.25/16
tve = 1/16
tae = .25/16
ts = .25/16

sersi = input("How many servings would you like to make?")
ss = int(sersi)

print(format(clew*ss, '.3f'), "cups large egg whites")
print(format(cs*ss, '.3f'), "cups sugar (divided)")
print(format(ccf*ss, '.3f'), "cups cake flour")
print(format(tct*ss, '.3f'), "teaspoons cream of tartar")
print(format(tve*ss, '.3f'), "teaspoons vanilla extract")
print(format(tae*ss, '.3f'), "teaspoons almond extract")
print(format(ts*ss, '.3f'), "teaspoons salt")
