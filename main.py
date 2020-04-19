from old import Old
from young import Young

A = Old('ram nreddy',74,'male')
B = Old('rajaram',62,'male')
C = Old('ram reddy',74,'male')
D = Old('sujatha',60,'female')
E = Old('swarupa',52,'Female')
F = Old('mahinder',55,'male')
Y = Young('deepika',22,'Female')
Z = Young('varun',22,'Female')
the_log ={}

for young in Young.young_list:
    if young.status:
        young.select(Old.old_list)
        for old in young.care_list_chosen:
            if(old.accept(young)):
                final = young.add_old(old)
                if final:
                    print("{} is taking care of {} aged {}".format(young.name,old.name,old.age))
                    the_log.setdefault(old.name,young.name)
                else:
                    print("{} cant take more than {} ".format(young.name,young.name))
                    young.set_status = False
                    old.set_status = True