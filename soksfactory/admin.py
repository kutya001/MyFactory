from django.contrib import admin

from adminclasses.adminOTHERS import TypeSpecialKeysAdmin, SpecialKeysAdmin
from soksfactory.adminclasses.adminINEM import (CounterpartyAdmin, DepartmentAdmin, 
                                                EmployesAdmin, IndividualsAdmin, 
                                                JobTitleAdmin)


#OTHERS
admin.site.register(TypeSpecialKeysAdmin)
admin.site.register(SpecialKeysAdmin)


#INEM
admin.site.register(CounterpartyAdmin)
admin.site.register(EmployesAdmin)
admin.site.register(DepartmentAdmin)
admin.site.register(JobTitleAdmin)
admin.site.register(IndividualsAdmin)



