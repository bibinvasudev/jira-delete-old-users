#!/usr/bin/env python
"""
Ansible Module for removing 'inactive' users from Jira
"""

from ansible.module_utils.basic import AnsibleModule
from jira import Jira


DOCUMENTATION = '''
---
module: jira_lib
short_description: Role to delete 'inactive' users that have not logged on for so many days
description:
    - Role to delete 'inactive' users that have not logged on for so many days
options:
    days:
        description:
            - Users that have not logged on for the number of 'days'
        required: False
    delete:
        description:
            - flag to specify whether to delete the users from jira
        required: False
'''

EXAMPLES = '''
- name: Delete jira users that have not logged on for 120 days
  jira_lib:
    days: "120"
    delete: True
  register: result
- debug:
    var:result

# set in vars or defaults...
user_whitelist:
  - abc123
  - def234

- name: |
    Delete Jira users that have not logged on for 175 days and provide a
    whitelist of users not to delete
  jira_lib:
    days: "175"
    delete: False
    user_whitelist: "{{ user_whitelist }}"
  register: result
- debug:
    var:result
'''

def main():

    fields = {
        "hostname": {"required": True, "type": "str"},
        "port": {"default": 1521, "type": 'int'},
        "service_name": {"required": False, "type": "str"},
        "user": {"required": False, "type": "str"},
        "password": {"required": False, "type": "str"},
        "service_name": {"required": False, "type": "str"},
        "days": {"required": False, "default": "90"},
        "delete": {"required": False, "default": "False"},

        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }

    module = AnsibleModule(argument_spec=fields)
    hostname = module.params['hostname']
    port = module.params['port']
    service_name = module.params['service_name']
    user = module.params['user']
    password = module.params['password']
    days = module.params['days']
    userlist = []
    if module.params['delete'] == 'True':
        jra = Jira(db_host=hostname, db_port=port, db_service_name=service_name, db_user=user, db_password=password)
        inactive_users = jra.get_inactive_users(days=days)
        for user in inactive_users:
            jra.delete_user(user)
            userlist.append(user)
    result = dict(changed=True, meta=userlist)
    module.exit_json(**result)

if __name__ == '__main__':
    main()