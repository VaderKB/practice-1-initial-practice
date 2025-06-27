import os

print('Env var GLOBAL_VAR_1 =', os.environ.get('GLOBAL_VAR_1', 'value not found'))
print('Env var GLOBAL_VAR_2 =', os.environ.get('GLOBAL_VAR_2', 'value not found'))
print('Env var FIRST_JOB_ENV_1 =', os.environ.get('FIRST_JOB_ENV_1', 'value not found'))
print('Env var FIRST_JOB_ENV_2 =', os.environ.get('FIRST_JOB_ENV_2', 'value not found'))
print('Env var SECOND_JOB_ENV_1 =', os.environ.get('SECOND_JOB_ENV_1', 'value not found'))
print('Env var SECOND_JOB_ENV_2 =', os.environ.get('SECOND_JOB_ENV_2', 'value not found'))