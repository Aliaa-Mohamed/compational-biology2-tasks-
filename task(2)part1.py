from cobra import Model,Reaction,Metabolite

model=Model('first_model')
v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1


v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000


v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000


m=Reaction('m')
m.name='m'
m.lower_bound=0
m.upper_bound=1000


glc=Metabolite('glc',compartment='c')
AA=Metabolite('AA',compartment='c')
biomath=Metabolite('biomath',compartment='c')



v0.add_metabolites({glc:1})
v1.add_metabolites({glc:-1,AA:1})
v2.add_metabolites({AA:-9.09,biomath:1})
m.add_metabolites({biomath:-1})
model.add_reactions([v0,v1,v2,m])
model.objective='m'
print(model.optimize())
print(model.summary())


