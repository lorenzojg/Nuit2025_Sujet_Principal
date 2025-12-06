
# # import du DAO avec un alias pour simplifier le reste du code de ce fichier
# # from app.models.PokemonDAO import PokemonJsonDAO as PokemonDAO
# from app.models.PokemonDAO import PokemonSqliteDAO as PokemonDAO

# class PokemonService():
# 	"""
# 	Class dedicated for the logic behind the pokemons
# 	"""
# 	def __init__(self):
# 		# cette ligne utilise le Data Access Object (DAO) dédié aux fichier JSON
# 		self.pdao = PokemonDAO()

# 	def getPokemonByNumber(self, num):
# 		res = self.pdao.findByNumber(num)
# 		# petit ajout : ici in verifie si res est une liste. Si ce n'est pas le cas, nous l'imbriquons dans une liste
# 		if type(res) is not list: 
# 			res = [res] 
# 		return res

# 	def getPokemonTypes(self):
# 		# cette logique est indépendante du type de stockage, ce qui est parfait pour 
# 		# illustrer le service. 
# 		# (évidemment nous aurions pu directement gérer les instances de classe Pokemon ici)
# 		types = set()
# 		for pokemon in self.pdao.findAll():
# 			types.add(pokemon.type1)

# 		return list(types)
	
# 	def getPokemonsByType(self, ptype):
# 		res = self.pdao.findByType(ptype)
# 		# petite vérification supplémentaire au cas où la liste est vide
# 		if len(res) > 0: return res
# 		return [{}]