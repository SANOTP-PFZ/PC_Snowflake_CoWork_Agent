TA_AGENTS = [
    {"name": "Pneumococcal (PCV)", "brand": "PCV", "desc": "Conversational querying across all Pneumococcal data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_PCV_VACCINE_AGENT"},
    {"name": "Respiratory Syncytial Virus (RSV)", "brand": "RSV", "desc": "Conversational querying across all Respiratory Syncytial Virus data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_RSV_VACCINE_AGENT"},
    {"name": "Flu", "brand": "FLU", "desc": "Conversational querying across all Flu data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_FLU_VACCINE_AGENT"},
    {"name": "Oral Anticoagulant (OAC)", "brand": "OAC", "desc": "Conversational querying across all Oral Anticoagulant data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OAC_AGENT"},
    {"name": "COVID", "brand": "COVID", "desc": "Conversational querying across all COVID data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_COVID_VACCINE_AGENT"},
    {"name": "Migraine (OCGRP)", "brand": "OCGRP", "desc": "Conversational querying across all Migraine data sources.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_MIGRAINE_AGENT"},
]

TAD_SHIPMENT_AGENTS = [
    {"name": "CDC Provider", "brand": "CDC", "tag": "CDC", "desc": "CDC provider-level administration data tracking and reporting for vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_CDC_PROVIDER_DOSES"},
    {"name": "CDC Bulk", "brand": "CDC", "tag": "CDC", "desc": "CDC bulk dose distribution data monitoring and aggregation for vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_CDC_BULK_SHIPMENTS"},
    {"name": "DDD Vaccines", "brand": "DDD", "tag": "DDD", "desc": "DDD wholesaler distribution data weekly demand and shipment insights for vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_DDD_VACCINES_WEEKLY"},
    {"name": "DDD IM", "brand": "DDD", "tag": "DDD", "desc": "DDD wholesaler distribution data weekly demand and shipment insights for Internal Medicine brands.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=DDD_SALES_WEEKLY"},
    {"name": "867 Vaccines", "brand": "867", "tag": "867", "desc": "867 EDI channel distribution data querying and reporting for vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_867_VACCINES"},
]

TAD_ADMINS_AGENTS = [
    {"name": "Elaad Covid", "source": "Elaad", "market": "Covid", "brand": "Covid", "desc": "eLAAD pharmacy and medical claims-based market tracking and insight generation for COVID vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=ELAAD_COVID_MARKET_AGENT"},
    {"name": "Elaad Rsv", "source": "Elaad", "market": "Rsv", "brand": "Rsv", "desc": "eLAAD pharmacy and medical claims-based performance monitoring and insights for RSV vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/agents/database/VAW_AMER_DESIGN/schema/USIMVACCINESSDL/agent/PC_ELAAD_RSV_VACCINES/details?tab=preview"},
    {"name": "Elaad Flu", "source": "Elaad", "market": "Flu", "brand": "Flu", "desc": "eLAAD pharmacy and medical claims-based performance monitoring and insights for Flu vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_FLU_VACCINES"},
    {"name": "Elaad Pcv", "source": "Elaad", "market": "Pcv", "brand": "Pcv", "desc": "eLAAD pharmacy and medical claims-based performance monitoring and insights for PCV.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_PCV_VACCINES"},
    {"name": "Optum Covid", "source": "Optum", "market": "Covid", "brand": "Covid", "desc": "Optum pharmacy and medical claims-based tracking and reporting for COVID vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_COVID_VACCINES"},
    {"name": "Optum Rsv", "source": "Optum", "market": "Rsv", "brand": "Rsv", "desc": "Optum pharmacy and medical claims-based analytics and reporting for RSV vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_RSV_VACCINES"},
    {"name": "Optum Flu", "source": "Optum", "market": "Flu", "brand": "Flu", "desc": "Optum pharmacy and medical claims-based analytics and reporting for Flu vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_FLU_VACCINES"},
    {"name": "Optum Pcv", "source": "Optum", "market": "Pcv", "brand": "Pcv", "desc": "Optum pharmacy and medical claims-based analytics and reporting for PCV.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_PCV_VACCINES"},
    {"name": "Health Verity Covid", "source": "Health Verity", "market": "Covid", "brand": "Covid", "desc": "HealthVerity pharmacy claims-based analytics and insight generation for COVID vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_COVID_VACCINES"},
    {"name": "Health Verity Rsv", "source": "Health Verity", "market": "Rsv", "brand": "Rsv", "desc": "HealthVerity pharmacy claims-based analytics and insight generation for RSV vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_RSV_VACCINES"},
    {"name": "Health Verity Flu", "source": "Health Verity", "market": "Flu", "brand": "Flu", "desc": "HealthVerity pharmacy claims-based analytics and insight generation for Flu vaccines.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_FLU_VACCINES"},
    {"name": "Health Verity Pcv", "source": "Health Verity", "market": "Pcv", "brand": "Pcv", "desc": "HealthVerity pharmacy claims-based analytics and insight generation for PCV.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_PCV_VACCINES"},
]

TAD_OAC_AGENTS = [
    {"name": "Elaad OAC", "brand": "OAC", "desc": "eLAAD pharmacy and medical claims-based market tracking and insights for OAC.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_OAC"},
    {"name": "Optum OAC", "brand": "OAC", "desc": "Optum pharmacy and medical claims-based analytics and reporting for the OAC portfolio.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_OAC"},
]

TAD_MIGRAINE_AGENTS = [
    {"name": "Migraine LAAD", "brand": "OCGRP", "desc": "LAAD pharmacy and medical claims-based weekly monitoring and trend surfacing for the Migraine portfolio.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USMIGRAINEIISRPTETL&agent=MIGRAINE_LAAD_W_AGENT"},
    {"name": "Migraine NPA", "brand": "OCGRP", "desc": "NPA prescription data querying and automated insight generation for Migraine brands.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=MIGRAINEDEEPDIVEDUPLICATE&agent=MIGRAINE_NPA_AGENT"},
    {"name": "Forsyth", "brand": "OCGRP", "desc": "Forsyth market research data querying and insight generation for the Migraine portfolio.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_FORSYTH_MIGRAINE"},
    {"name": "Migraine Elaad", "brand": "OCGRP", "desc": "Monthly Elaad aggregation for migraine.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai"},
]

TAD_NPA_AGENTS = [
    {"name": "NPA TRx", "brand": "NPA", "desc": "NPA prescription data-based TRx performance tracking across all brands.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USPRIMARYCAREADHOCANALYTICSPARTC&agent=PC_NPA_TRX_ALL_BRANDS"},
    {"name": "NPA NBRx", "brand": "NPA", "desc": "NPA prescription data-based NBRx acquisition trends and insight generation across all brands.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USPRIMARYCAREADHOCANALYTICSPARTC&agent=PC_NPA_NBRX_ALL_BRANDS"},
]

TAD_COPAY_AGENTS = [
    {"name": "CoPay", "brand": "CoPay", "desc": "Copay redemption transaction data analytics and program performance insights across brands.", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_COPAY_REDEMPTION_AGENT"},
]
