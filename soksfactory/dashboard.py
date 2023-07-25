# from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard

# class CustomIndexDashboard(Dashboard):
#     def init_with_context(self, context):
#         # Добавьте свои кастомные виджеты или модули здесь
#         self.children.append(modules.Group(
#             title='Group 1',
#             display='tabs',  # или 'stacked' для стекового отображения
#             children=[
#                 AppIndexDashboard(),
#             ]
#         ))

#         self.children.append(modules.ModelList(
#             title='Group 2',
#             models=('soksfactory.models.modelsOTHERS.TypeSpecialKeys'),
#         ))