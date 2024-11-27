# %{{cookiecutter.display_name}}%

Dobrodošli u %{{cookiecutter.display_name}}%! sadrži ključne informacije za postavljanje CI/CD pipeline-a, deploymenta i razumijevanja ključnih konfiguracija aplikacije.

---

## 1. Pregled projekta
[//]: # (TODO: ispuniti)
- **Svrha Projekta**: <Kratki opis čemu projekt služi.>
- **Tehnološki Stack**: <Jezici, okviri, baze podataka, itd.>
- [**Postavljanje razvojnog okruženja**](development.md)

---

## 2. Informacije potrebne za postavljanje CI/CD-a

### Kontinuirana integracija (CI)
1. **Proces Izgradnje**:
    - Skripta za izradu arhive: `%{{cookiecutter.build_script}}%`
    - Skripta za kontejnerizaciju: `%{{cookiecutter.containerize_script}}%` 

### Kontinuirani deployment (CD)

1. **Ciljana okruženja**:
    - Izvršna okruženja: 
       - [{% if cookiecutter.target_env_Dev == "Y" %}x{% else %} {% endif %}] Dev
       - [{% if cookiecutter.target_env_Test == "Y" %}x{% else %} {% endif %}] Test
       - [{% if cookiecutter.target_env_UAT == "Y" %}x{% else %} {% endif %}] UAT
       - [{% if cookiecutter.target_env_Prod == "Y" %}x{% else %} {% endif %}] Prod

2. **Konfiguracijske datoteke**:

[//]: # (TODO: ispuniti)

Lokacije na kojima se trebaju postaviti konfiguracijske datoteke u ovisnosti o 
okolinama. Moguće je navesti 0 do x lokacija.

Dev: 
```yaml
- name: nazivDatoteke.ekstenzija
  value: lokacija
``` 

Test:
```yaml
- name: nazivDatoteke.ekstenzija
  value: lokacija
``` 

UAT:
```yaml
- name: nazivDatoteke.ekstenzija
  value: lokacija
``` 

Prod:
```yaml
- name: nazivDatoteke.ekstenzija
  value: lokacija
``` 

---

## 3. Ovisnosti aplikacije

### Međuovisnosti
[//]: # (TODO: ispuniti)
Ova aplikacija ovisi o sljedećim aplikacijama ili sustavima:

```yaml
dependsOn:
  - name: <naziv aplikacije ili sustava>
```

---

## 4. Konfiguracija za Kubernetes

### Zahtjevi za resurse
1. **CPU i memorija**:
    - Zadano: %{{cookiecutter.default_cpu}}% CPU, %{{cookiecutter.default_memory}}%
    - Limiti: %{{cookiecutter.limit_cpu}}% CPU, %{{cookiecutter.limit_memory}}%

2. **Pohrana**:
    - Perzistentna pohrana podataka: %{{cookiecutter.storage_claims}}%
    - Baza podataka: {% if cookiecutter.database == "Y" %} Da{% else %}Ne{% endif %}
    {%- if cookiecutter.database == "Y" %}

    [//]: # (TODO: navedite tipove potrebnih baza podataka)
      - [ ] MSSQL
      - [ ] GraphDB
    {%- endif %}

### Konfiguracija podova
1. **Varijable okruženja**:
    - Ključ-vrijednost parovi: %{{cookiecutter.env_variables}}% 
    - Tajne vrijednosti (secreti) se koriste: {% if cookiecutter.secrets_management_tool == "Y" %}Da{% else %}Ne{% endif %}

2. **Konfiguracijske datoteke**:
    - Lokacije montiranja/postavljanja: %{{cookiecutter.config_mount_path}}% 
    - Primjeri: %{{cookiecutter.config_examples}}% 

{% set network_access_rules_list = cookiecutter.network_access_rules.split(',') %}
{% set exposed_ports_list = cookiecutter.exposed_ports.split(',') %}
3. **Mreža**:
    - Izloženi portovi: %{{cookiecutter.exposed_ports}}%
      {%- for port in exposed_ports_list %}
        - `%{{ port.strip() }}%`
      {%- endfor %}
    - Pravila pristupa prema vanjskom svijetu:
      {%- for access in network_access_rules_list %}
        - `%{{ access.strip() }}%`
      {%- endfor %}

---

## 5. Dodatni zahtjevi

1. **Nadzor**:
    - Logovi u JSON formatu: {% if cookiecutter.json_logging_compatible == "Y" %} Da{% else %}Ne{% endif %}

2. **Skaliranje**:
    - Zadani broj replika: %{{cookiecutter.default_replicas}}% 
    - HPA (automatsko horizontalno skaliranje) Konfiguracija: %{{cookiecutter.hpa_thresholds}}% 

3. **Sigurnost**:
    - Upravljanje tajnama: {% if cookiecutter.secrets_management_tool == "Y" %}Da{% else %}Ne{% endif %}

4. **Testiranje**:

   Lokacije skripti za izvršavanje testova (ako postoje):
     - unit: `%{{cookiecutter.unit_test_script_location}}%`
     - integracijski: `%{{cookiecutter.integration_test_script_location}}%`
     - performansni: `%{{cookiecutter.performance_test_script_location}}%`

---

## 6. Kontakti i podrška

{% set team_leads_list = cookiecutter.team_leads.split(',') %}

**Voditelji tima**:
{%- for lead in team_leads_list %}
  - %{{ lead.strip() }}%
{% endfor %}