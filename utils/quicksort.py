# quick sort implementation with sorting bounds and a comparator

def quicksort(list, left, right, comparator)
	i = left
	j = right
	pivot = list[int((i + j)/2)]

	while i <= j:
		while comparator(list[i], pivot) and i < len(list)
			i += 1
		while comparator(pivot, list[i]) and j > -1:
			j -= 1
		if i <= j:
			# swap
			tmp = list[j]
			list[j] = list[i]
			list[i] = tmp
			i += 1
			j -= 1
	
	if left < j:
		quicksort(list, left, j, comparator)
	if i < right:
		quicksort(list, i, right, comparator)

# comparator implementations for the various program features
# These functions return True if the first parameter is considered greater than the second parameter and false otherwise

# Tabela 1
# Ordem	Categoria
# 1		Medicina
# 2		Enfermagem
# 3		Auxiliar

# Tabela 2
# Ordem Faixa Etária
# 1		Jovem
# 2		Adulto
# 3		Idoso

# Ordem	Serviço			Anterior	Posterior
# 1		Consulta		-			-
# 2		PequenaCirurgia	Consulta	Consulta
# 3		Enfermagem		-			-

# Listar profissionais (LP) Lista todos os profissionais de saúde por categoria, e por
# ordem alfabética dentro de cada categoria. As categorias devem ser listadas de acordo com a ordem
# apresentada na Tabela 1. 

def lp_comparator(proA, proB)
	proA_category = proA.categoria # assuming this is the integer with the category id
	proB_category = proB.categoria

	if proA_category == proB_category:
		# Untie by alphabetic order
		return proA.name >= proB.name

	# Untie by category
	return proA_category > proB_category

# Listar utentes (LU) Lista todos os utentes por ordem alfabética de família, por
# faixa etária em cada família, e por ordem alfabética de nome dentro de cada faixa etária. As faixas
# etárias devem ser listadas de acordo com a ordem apresentada na Tabela 2. Se um utente não
# tiver família associada, deve ser só indicada a faixa etária.

def lu_comparator(utA, utB)
	utA_fam = utA.family
	utB_fam = utB.family
	utA_age_range = utA.age_range # assuming this is the age range id
	utB_age_range = utB.age_range

	# only one user has no family, users with family are considered greater than those without
	if (utA_fam == None and utB_fam != None) or (utA_fam != None and utB_fam == None):
		return True if utB_fam == None else False

	if (utA_fam == None and utB_fam == None) or utA_fam.name == utB_fam.name: 
		if utA_age_range == utB_age_range:
			# Untie by name alphabetic order
			return utA.name > utB.name

		# Untie by age range
		return utA_age_range > utB_age_range

	# Untie by family name
	return utA_fam.name > utB_fam.name

# Listar famílias (LF)Lista todas as famílias por ordem alfabética

def lf_comparator(famA, famB)
	return famA.name > famB.name

# Mostrar família (MF) Lista todos os utentes de uma família, por ordem de faixa etária, 
# e por ordem alfabética dentro de cada faixa etária. As faixas etárias devem ser listadas de
# acordo com a ordem apresentada na Tabela 2.

def mf_comparator(utA, utB)
	utA_age_range = utA.age_range # assuming this is the age range id
	utB_age_range = utB.age_range

	if utA_age_range == utB_age_range:
		# Untie by name
		return utA.name > utB.name

	# Untie by age range
	return utA_age_range > utB_age_range

# Listar cuidados marcados a utente (LCU) Listar todos os serviços marcados a
# um utente, por ordem de serviço, por ordem de categoria por cada serviço, e por ordem alfabética
# de nome de profissional por cada categoria. Os serviços devem ser listados de acordo com a ordem
# apresentada na Tabela 3. As categorias devem ser listadas de acordo com a ordem apresentada na
# Tabela 1. Os serviços com a mesma ordem devem ser apresentados pela ordem de marcação.

def lcu_comparator(srvA, srvB)
	# assuming "ordem de serviço" means order by service type
	srvA_type = srvA.type # assuming this is the service type id
	srvB_type = srvB.type
	srvA_category = srvA.category # assuming this is the category id
	srvB_category = srvB.category

	if srvA_type == srvB_type:
		if srvA_category == srvB_category:
			# Untie by professional name alphabetically
			return srvA.professional > srvB.professional

		# Untie by category
		return srvA_category > srvB_category

	# Untie by service type
	return srvA_type > srvB_type

# Listar cuidados marcados a família (LCF) Listar o resultado da instrução LCU
# para cada utente membro da família, por ordem de faixa etária, e ordem alfabética de nome de
# utente por cada faixa etária. As faixas etárias devem ser listadas de acordo com a ordem
# apresentada na Tabela 2.

def lcf_comparator(utA, utB)
	utA_age_range = utA.age_range # assuming this is the age range id
	utB_age_range = utB.age_range

	if utA_age_range == utB_age_range: 
		return utA.name > utB.name

	# Untie by age range
	return utA_age_range > utB_age_range

# Listar serviços marcados a profissional (LSP) Listar todos os serviços marcados
# a um profissional de saúde, por ordem de tipo de serviço, e por ordem alfabética de nome de
# utente por tipo de serviço. Os serviços devem ser listados de acordo com a ordem apresentada na Tabela 3. 

def lsp_comparator(srvA, srvB)
	srvA_type = srvA.type # assuming this is the service type id
	srvB_type = srvB.type

	if srvA_type == srvB_type:
		return srvA.utente.name > srvB.utente.name

	# Untie by service type
	return srvA_type > srvB_type

# Listar marcações por tipo de serviço (LMS) Listar todos os serviços marcados
# de um determinado tipo, por ordem de categoria profissional, por ordem alfabética de nome de
# profissional em cada categoria, e por ordem alfabética de nome de utente por cada profissional.
# As categorias devem ser listadas de acordo com a ordem apresentada na Tabela 1.

def lms_comparator(srvA, srvB)
	srvA_category = srvA.category # assuming this is the category id
	srvB_category = srvB.category # assuming this is the category id
	srvA_pro_name = srvA.professional.name
	srvB_pro_name = srvB.professional.name

	if srvA_category == srvB_category:
		if srvA_pro_name == srvB_pro_name: 
			return srvA.utente.name > srvB.utente.name

		# Untie by pro name alphabetically
		return srvA_pro_name > srvB_pro_name

	# Untie by category
	return srvA_category > srvB_category
