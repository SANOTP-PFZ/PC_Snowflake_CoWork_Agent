BRANDS = [
    {"name": "Nurtec", "category": "Migraine", "trend": "+6.2%", "direction": "up", "values": [20, 17, 18, 11, 9, 5]},
    {"name": "Eliquis", "category": "Anticoagulation", "trend": "+2.1%", "direction": "up", "values": [16, 15, 17, 13, 12, 10]},
    {"name": "Abrysvo", "category": "RSV vaccine", "trend": "-3.4%", "direction": "down", "values": [8, 10, 9, 14, 16, 19]},
    {"name": "Comirnaty", "category": "COVID-19 vaccine", "trend": "-8.5%", "direction": "down", "values": [6, 9, 12, 14, 18, 22]},
    {"name": "Prevnar", "category": "Pneumococcal", "trend": "+1.8%", "direction": "up", "values": [18, 16, 17, 14, 13, 11]},
]

TA_AGENTS = [
    {"name": "PCV agent", "brand": "PCV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_PCV_VACCINE_AGENT"},
    {"name": "RSV agent", "brand": "RSV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_RSV_VACCINE_AGENT"},
    {"name": "FLU agent", "brand": "FLU", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_FLU_VACCINE_AGENT"},
    {"name": "OAC agent", "brand": "OAC", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OAC_AGENT"},
    {"name": "COVID agent", "brand": "COVID", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_COVID_VACCINE_AGENT"},
    {"name": "OCGRP agent", "brand": "OCGRP", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_MIGRAINE_AGENT"},
]

TAD_SHIPMENT_AGENTS = [
    {"name": "CDC Provider agent", "brand": "CDC", "tag": "CDC", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_CDC_PROVIDER_DOSES"},
    {"name": "CDC Bulk agent", "brand": "CDC", "tag": "CDC", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_CDC_BULK_SHIPMENTS"},
    {"name": "DDD Vaccines agent", "brand": "DDD", "tag": "DDD", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_DDD_VACCINES_WEEKLY"},
    {"name": "DDD IM agent", "brand": "DDD", "tag": "DDD", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=DDD_SALES_WEEKLY"},
    {"name": "867 Vaccines agent", "brand": "867", "tag": "867", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_867_VACCINES"},
]

TAD_ADMINS_AGENTS = [
    {"name": "ELAAD COVID agent", "source": "ELAAD", "market": "COVID", "brand": "COVID", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=ELAAD_COVID_MARKET_AGENT"},
    {"name": "ELAAD RSV agent", "source": "ELAAD", "market": "RSV", "brand": "RSV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/agents/database/VAW_AMER_DESIGN/schema/USIMVACCINESSDL/agent/PC_ELAAD_RSV_VACCINES/details?tab=preview"},
    {"name": "ELAAD FLU agent", "source": "ELAAD", "market": "FLU", "brand": "FLU", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_FLU_VACCINES"},
    {"name": "ELAAD PCV agent", "source": "ELAAD", "market": "PCV", "brand": "PCV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_PCV_VACCINES"},
    {"name": "ELAAD OAC agent", "source": "ELAAD", "market": "OAC", "brand": "OAC", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_ELAAD_OAC"},
    {"name": "OPTUM COVID agent", "source": "OPTUM", "market": "COVID", "brand": "COVID", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_COVID_VACCINES"},
    {"name": "OPTUM RSV agent", "source": "OPTUM", "market": "RSV", "brand": "RSV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_RSV_VACCINES"},
    {"name": "OPTUM FLU agent", "source": "OPTUM", "market": "FLU", "brand": "FLU", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_FLU_VACCINES"},
    {"name": "OPTUM PCV agent", "source": "OPTUM", "market": "PCV", "brand": "PCV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_PCV_VACCINES"},
    {"name": "OPTUM OAC agent", "source": "OPTUM", "market": "OAC", "brand": "OAC", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_OPTUM_OAC"},
    {"name": "HEALTH VERITY COVID agent", "source": "HEALTH VERITY", "market": "COVID", "brand": "COVID", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_COVID_VACCINES"},
    {"name": "HEALTH VERITY RSV agent", "source": "HEALTH VERITY", "market": "RSV", "brand": "RSV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_RSV_VACCINES"},
    {"name": "HEALTH VERITY FLU agent", "source": "HEALTH VERITY", "market": "FLU", "brand": "FLU", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_FLU_VACCINES"},
    {"name": "HEALTH VERITY PCV agent", "source": "HEALTH VERITY", "market": "PCV", "brand": "PCV", "url": "https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai/chat/new?db=VAW_AMER_DESIGN&schema=USIMVACCINESSDL&agent=PC_HV_PCV_VACCINES"},
]

BRAND_FILTERS = ["All", "PCV", "RSV", "FLU", "OAC", "COVID", "OCGRP"]
SOURCE_FILTERS = ["All sources", "Shipment", "Admins"]
