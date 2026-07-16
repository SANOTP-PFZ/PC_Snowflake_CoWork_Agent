TA_AGENTS = [
    {"name": "Pneumococcal (PCV)", "brand": "PCV", "desc": "Conversational querying across all PCV vaccine data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_PCV_VACCINE_AGENT"},
    {"name": "Respiratory Syncytial Virus (RSV)", "brand": "RSV", "desc": "RSV vaccine analytics and automated insight generation.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_RSV_VACCINE_AGENT"},
    {"name": "Flu", "brand": "FLU", "desc": "Flu vaccine data querying and trend surfacing.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_FLU_VACCINE_AGENT"},
    {"name": "Oral Anticoagulant (OAC)", "brand": "OAC", "desc": "OAC market and claims data exploration.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OAC_AGENT"},
    {"name": "COVID", "brand": "COVID", "desc": "COVID vaccine performance and market share analytics.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_COVID_VACCINE_AGENT"},
    {"name": "Migraine (OCGRP)", "brand": "OCGRP", "desc": "Migraine therapy area data and competitive insights.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_MIGRAINE_AGENT"},
]

TAD_SHIPMENT_AGENTS = [
    {"name": "CDC Provider", "brand": "CDC", "tag": "CDC", "desc": "CDC provider-level dose shipment data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_CDC_PROVIDER_DOSES"},
    {"name": "CDC Bulk", "brand": "CDC", "tag": "CDC", "desc": "CDC bulk shipment tracking and analysis.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_CDC_BULK_SHIPMENTS"},
    {"name": "DDD Vaccines", "brand": "DDD", "tag": "DDD", "desc": "Weekly DDD vaccines sales data processing.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_DDD_VACCINES_WEEKLY"},
    {"name": "DDD IM", "brand": "DDD", "tag": "DDD", "desc": "DDD internal medicine sales weekly.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=DDD_SALES_WEEKLY"},
    {"name": "867 Vaccines", "brand": "867", "tag": "867", "desc": "867 vaccine inventory and distribution data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_867_VACCINES"},
]

TAD_ADMINS_AGENTS = [
    {"name": "Elaad Covid", "source": "Elaad", "market": "Covid", "brand": "Covid", "desc": "Elaad COVID administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=ELAAD_COVID_MARKET_AGENT"},
    {"name": "Elaad Rsv", "source": "Elaad", "market": "Rsv", "brand": "Rsv", "desc": "Elaad RSV administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/agents/database/VAW_AMER_DESIGN/schema/USIMVACCINESSDL/agent/PC_ELAAD_RSV_VACCINES/details?tab=preview"},
    {"name": "Elaad Flu", "source": "Elaad", "market": "Flu", "brand": "Flu", "desc": "Elaad Flu administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_FLU_VACCINES"},
    {"name": "Elaad Pcv", "source": "Elaad", "market": "Pcv", "brand": "Pcv", "desc": "Elaad PCV administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_PCV_VACCINES"},
    {"name": "Optum Covid", "source": "Optum", "market": "Covid", "brand": "Covid", "desc": "Optum COVID administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_COVID_VACCINES"},
    {"name": "Optum Rsv", "source": "Optum", "market": "Rsv", "brand": "Rsv", "desc": "Optum RSV administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_RSV_VACCINES"},
    {"name": "Optum Flu", "source": "Optum", "market": "Flu", "brand": "Flu", "desc": "Optum Flu administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_FLU_VACCINES"},
    {"name": "Optum Pcv", "source": "Optum", "market": "Pcv", "brand": "Pcv", "desc": "Optum PCV administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_PCV_VACCINES"},
    {"name": "Health Verity Covid", "source": "Health Verity", "market": "Covid", "brand": "Covid", "desc": "Health Verity COVID administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_COVID_VACCINES"},
    {"name": "Health Verity Rsv", "source": "Health Verity", "market": "Rsv", "brand": "Rsv", "desc": "Health Verity RSV administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_RSV_VACCINES"},
    {"name": "Health Verity Flu", "source": "Health Verity", "market": "Flu", "brand": "Flu", "desc": "Health Verity Flu administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_FLU_VACCINES"},
    {"name": "Health Verity Pcv", "source": "Health Verity", "market": "Pcv", "brand": "Pcv", "desc": "Health Verity PCV administrations data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_PCV_VACCINES"},
]

TAD_OAC_AGENTS = [
    {"name": "Elaad OAC", "brand": "OAC", "desc": "Elaad OAC claims and market data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_OAC"},
    {"name": "Optum OAC", "brand": "OAC", "desc": "Optum OAC claims and market data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_OAC"},
]

TAD_MIGRAINE_AGENTS = [
    {"name": "Migraine LAAD", "brand": "OCGRP", "desc": "Weekly LAAD data processing and trend surfacing.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USMIGRAINEIISRPTETL&agent=MIGRAINE_LAAD_W_AGENT"},
    {"name": "Migraine NPA", "brand": "OCGRP", "desc": "Conversational NPA data querying for migraine.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=MIGRAINEDEEPDIVEDUPLICATE&agent=MIGRAINE_NPA_AGENT"},
    {"name": "Forsyth", "brand": "OCGRP", "desc": "Forsyth migraine analytics and reporting.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_FORSYTH_MIGRAINE"},
    {"name": "Migraine Elaad", "brand": "OCGRP", "desc": "Monthly Elaad aggregation for migraine.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai"},
]

TAD_NPA_AGENTS = [
    {"name": "NPA TRx", "brand": "NPA", "desc": "National prescription audit TRx data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USPRIMARYCAREADHOCANALYTICSPARTC&agent=PC_NPA_TRX_ALL_BRANDS"},
    {"name": "NPA NBRx", "brand": "NPA", "desc": "National prescription audit NBRx data.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USPRIMARYCAREADHOCANALYTICSPARTC&agent=PC_NPA_NBRX_ALL_BRANDS"},
]

TAD_COPAY_AGENTS = [
    {"name": "CoPay", "brand": "CoPay", "desc": "CoPay redemption analysis and reporting.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_COPAY_REDEMPTION_AGENT"},
]
