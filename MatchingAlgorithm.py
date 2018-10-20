import math

'''
Params:
    student: a student
    teachers: a collection of teachers
    matching_objective_fns: an iterable collection of functions that accept arguments of the form:
            (student, teacher) and returns a numerical (int/double) suitability score, where a higher
            score means that the teacher is more suitable for the student with respect to the objective
            that we're trying to optimize.
    max_choices: the max number of teachers to return as potential matches
Returns: a list (w/ length <= max_choices) of potential teachers for the student to match with
'''
def get_matches_for_student(student, teachers, matching_objective_fns, max_choices):
    matches_to_fill = max_choices
    matches = list()
    pareto_fronts = get_pareto_fronts(teachers, student, matching_objective_fns)
    current_front_num = 0
    while current_front_num < len(pareto_fronts) and matches_to_fill >= len(pareto_fronts[current_front_num]):
        matches += pareto_fronts[current_front_num]
        matches_to_fill -= len(pareto_fronts[current_front_num])
        current_front_num += 1
    if current_front_num < len(pareto_fronts) and matches_to_fill != 0:
        matches += partial_selection_from_front(pareto_fronts[current_front_num], matches_to_fill, student, matching_objective_fns)
    return matches


def get_pareto_fronts(teachers, student, objective_fns):
    dominated_sets = dict() #maps teachers t to the set of teachers that t dominates
    domination_counts = dict() #maps teachers t to the number (int) of teachers that dominate t
    pareto_fronts = list()
    pareto_fronts.append(list()) #add the 0th pareto front (the pareto front of the entire data)
    for p in teachers:
        dominated_sets[p] = set()
        domination_counts[p] = 0
        for q in teachers:
            if p == q: continue
            dom = get_domination(p, q, student, objective_fns);
            if dom == -1: dominated_sets[p].add(q)
            elif dom == 1: domination_counts[p] += 1
        if domination_counts[p] == 0:
            pareto_fronts[0].append(p)
    i = 0
    while i < len(pareto_fronts):
        next_front = list()
        for p in pareto_fronts[i]:
            for q in dominated_sets[p]:
                domination_counts[q] -= 1
                if domination_counts[q] == 0:
                    next_front.append(q)
        i += 1
        if len(next_front) != 0:
            pareto_fronts.append(next_front)
    return pareto_fronts


'''
returns -1 if p dominates q, 1 if q dominates p, 0 otherwise
'''
def get_domination(teacher_p, teacher_q, student, objective_fns):
    pdomq = True;
    qdomp = True;
    for o in objective_fns:
        pscore = o(student, teacher_p)
        qscore = o(student, teacher_q)
        if pdomq and pscore < qscore: pdomq = False
        if qdomp and qscore < pscore: qdomp = False
    if pdomq and qdomp: return 0 #p and q have equal suitability scores for all objectives
    if pdomq: return -1
    if qdomp: return 1
    return 0


def partial_selection_from_front(front, num_elems_to_select, student, objective_fns):
    if num_elems_to_select >= len(front): return front #If this condition is true, this function should never be called
    distances = dict()
    for teacher in front: distances[teacher] = 0
    for o in objective_fns:
        obj_ordered_front = list(front)
        obj_ordered_front.sort(key=lambda teacher: o(student, teacher))
        distances[obj_ordered_front[0]] = float("inf")
        distances[obj_ordered_front[-1]] = float("inf")
        min_score = o(student, obj_ordered_front[0])
        max_score = o(student, obj_ordered_front[-1])
        for i in range(1, len(obj_ordered_front) - 1):
            obj_dist = o(student, obj_ordered_front[i+1]) - o(student, obj_ordered_front[i-1])
            norm_obj_dist = obj_dist/(max_score - min_score)
            distances[obj_ordered_front[i]] += norm_obj_dist

    dist_ordered_front = list(front)
    dist_ordered_front.sort(key=lambda teacher: distances[teacher])
    return dist_ordered_front[len(dist_ordered_front) - num_elems_to_select: len(dist_ordered_front)]

#def o1(s,t): return t[0]
#def o2(s,t): return t[1]
#teachers = [(2,0), (1,1), (0,2), (1,0),(0.6,0.4),(0.5,0.5),(0.4,0.6),(0,1)]
#print(get_matches_for_student(None, teachers, [o1, o2], 50))

