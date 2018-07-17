# Delete inactive  Jira Users
Role to delete inactive users from Jira


## Dependencies
It requires the oracle instant client to be installed in the python/ansible environment.

To install:
```
  - role: oracle-instantclient-install
    src: git+http://git......./scm/ansible/oracle-instantclient-install.git
```

## Example Playbook

For example to list all users that have not logged onto jira for more than 120 days:

```
- hosts: localhost
  connection: local

  roles:
    - jira-delete-old-users

  tasks:
    - jira_lib:
        delete: False
        days: 120
      register: result
    - debug: var=result
```

## Test

```
molecule test
```

## License

Internal

## Author Information

This role is maintained by the Bibin
