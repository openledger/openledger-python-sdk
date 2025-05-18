# Reference
## Banks
<details><summary><code>client.banks.<a href="src/openledger/banks/client.py">create_a_bank_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new Plaid link token for connecting a bank account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.banks.create_a_bank_link(entity_id='ent_123456', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to create the link token for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.banks.<a href="src/openledger/banks/client.py">add_bank_accounts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds new bank accounts using a Plaid public token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.banks.add_bank_accounts(entity_id='ent_123456', public_token='public-sandbox-123456-abcdef', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to add the bank accounts for
    
</dd>
</dl>

<dl>
<dd>

**public_token:** `str` — The Plaid public token received from the Plaid Link onSuccess callback
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Categories
<details><summary><code>client.categories.<a href="src/openledger/categories/client.py">get_categories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all categories
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.categories.get_categories(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/openledger/categories/client.py">create_a_new_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new category for the specified entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.categories.create_a_new_category(entity_id='entityId', name='name', type="ASSET", )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to create the category for
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the category
    
</dd>
</dl>

<dl>
<dd>

**type:** `PostV1CategoriesRequestType` 

The type of category. Must be one of:
* ASSET - For asset accounts
* LIABILITY - For liability accounts
* EQUITY - For equity accounts
* REVENUE - For revenue accounts
* EXPENSE - For expense accounts
    
</dd>
</dl>

<dl>
<dd>

**sub_type_code:** `typing.Optional[int]` — Optional subtype code for the category
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Developers
<details><summary><code>client.developers.<a href="src/openledger/developers/client.py">generate_developer_authentication_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a JWT token for developer authentication
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.developers.generate_developer_authentication_token(developer_id='developerId', api_key='apiKey', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**developer_id:** `str` — The ID of the developer
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — The API key for the developer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities
<details><summary><code>client.entities.<a href="src/openledger/entities/client.py">generate_authentication_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a JWT token for entity authentication
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.entities.generate_authentication_token(entity_id='entityId', api_key='apiKey', developer_id='developerId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — The API key for the entity
    
</dd>
</dl>

<dl>
<dd>

**developer_id:** `str` — The ID of the developer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/openledger/entities/client.py">get_entity_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a specific entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.entities.get_entity_details()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` — ID of the entity to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/openledger/entities/client.py">create_a_new_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new entity with the provided details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.entities.create_a_new_entity(developer_id='{{developerId}}', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**developer_id:** `str` — ID of the developer creating the entity
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — External identifier for the entity
    
</dd>
</dl>

<dl>
<dd>

**legal_name:** `typing.Optional[str]` — Legal name of the entity
    
</dd>
</dl>

<dl>
<dd>

**tin:** `typing.Optional[str]` — Tax Identification Number
    
</dd>
</dl>

<dl>
<dd>

**us_state:** `typing.Optional[str]` — US state code
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` — Type of entity
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Contact phone number
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Current status of the entity
    
</dd>
</dl>

<dl>
<dd>

**clerk_id:** `typing.Optional[str]` — Clerk ID (alternative to developerId)
    
</dd>
</dl>

<dl>
<dd>

**date_created:** `typing.Optional[dt.datetime]` — When the entity was created
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `typing.Optional[str]` — ID of the instance to associate with the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/openledger/entities/client.py">update_an_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing entity's details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.entities.update_an_entity(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — ID of the entity to update
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — External identifier for the entity
    
</dd>
</dl>

<dl>
<dd>

**legal_name:** `typing.Optional[str]` — Legal name of the entity
    
</dd>
</dl>

<dl>
<dd>

**tin:** `typing.Optional[str]` — Tax Identification Number
    
</dd>
</dl>

<dl>
<dd>

**us_state:** `typing.Optional[str]` — US state code
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` — Type of entity
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Contact phone number
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Current status of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/openledger/entities/client.py">delete_an_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing entity and its associated data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.entities.delete_an_entity(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — ID of the entity to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/openledger/entities/client.py">get_entities_by_developer_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all entities associated with a specific developer
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.entities.get_entities_by_developer_id(developer_id='developerId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**developer_id:** `str` — ID of the developer whose entities to retrieve
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of entities to return per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations
<details><summary><code>client.integrations.<a href="src/openledger/integrations/client.py">get_integration_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the status of all integrations for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.integrations.get_integration_status(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to get integration status for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/openledger/integrations/client.py">connect_an_integration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates the connection process for a third-party integration using the Unified API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.integrations.connect_an_integration(provider='quickbooks', entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `str` — The integration provider (e.g., quickbooks, xero)
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to connect the integration for
    
</dd>
</dl>

<dl>
<dd>

**connection_type:** `typing.Optional[str]` — The type of connection to establish (used as scope in Unified API)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/openledger/integrations/client.py">disconnect_an_integration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnects an existing integration for an entity by removing it from the Unified Connections table
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.integrations.disconnect_an_integration(entity_id='entityId', integration_type='integrationType', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity that owns the integration
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `str` — The type of integration to disconnect (must match connectionType in Unified Connections)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reports
<details><summary><code>client.reports.<a href="src/openledger/reports/client.py">generate_financial_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates comprehensive financial statements for an entity, including balance sheet, income statement, and cash flow statement
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.reports.generate_financial_reports(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to generate reports for
    
</dd>
</dl>

<dl>
<dd>

**month:** `typing.Optional[int]` — Month number (1-12) for the report period
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — Year for the report period (e.g., 2024)
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetV1ReportsGenerateRequestType]` — Type of report to generate
    
</dd>
</dl>

<dl>
<dd>

**ledger_id:** `typing.Optional[str]` — Optional ledger ID (if not provided, will use entityId)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/openledger/reports/client.py">get_general_ledger_report</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a detailed general ledger report with account balances and journal entries
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.reports.get_general_ledger_report(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to generate the report for
    
</dd>
</dl>

<dl>
<dd>

**month:** `typing.Optional[int]` — Month number (1-12) for the report period
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — Year for the report period (e.g., 2024)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/openledger/reports/client.py">get_financial_overview</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a high-level overview of financial data including balances, trends, and key metrics
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.reports.get_financial_overview(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to get the overview for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date for the report period
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date for the report period (defaults to current date)
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[GetV1ReportsOverviewRequestInterval]` — Time interval for aggregating data
    
</dd>
</dl>

<dl>
<dd>

**status_filter:** `typing.Optional[GetV1ReportsOverviewRequestStatusFilter]` — Filter transactions by their status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transactions
<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">get_transactions_by_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all transactions for a specific entity with pagination
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.get_transactions_by_entity(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to get transactions for
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of transactions per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">create_a_new_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new transaction for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.create_a_new_transaction(entity_id='entityId', amount=1.1, debit_account_id='debitAccountId', credit_account_id='creditAccountId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to create the transaction for
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — The amount of the transaction
    
</dd>
</dl>

<dl>
<dd>

**debit_account_id:** `str` — ID of the account to debit
    
</dd>
</dl>

<dl>
<dd>

**credit_account_id:** `str` — ID of the account to credit
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.datetime]` — When the transaction occurred (defaults to current time if not provided)
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency of the transaction
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the transaction
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PostV1TransactionsRequestStatus]` — Status of the transaction
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional transaction metadata
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">delete_a_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.delete_a_transaction(entity_id='entityId', transaction_id='transactionId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity that owns the transaction
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — The ID of the transaction to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">edit_a_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an existing transaction by updating its accounts and/or description
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.edit_a_transaction(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the transaction to edit
    
</dd>
</dl>

<dl>
<dd>

**debit_account_id:** `typing.Optional[str]` — ID of the account to debit (optional if credit_account_id is provided)
    
</dd>
</dl>

<dl>
<dd>

**credit_account_id:** `typing.Optional[str]` — ID of the account to credit (optional if debit_account_id is provided)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New description for the transaction
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">approve_one_or_multiple_transactions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve pending transactions by posting them to the ledger. Supports both single and batch transaction approval.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.approve_one_or_multiple_transactions(entity_id='entityId', request='tx_1234567890abcdef', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity that owns the transactions
    
</dd>
</dl>

<dl>
<dd>

**request:** `PutV1TransactionsApproveRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">get_transactions_by_month</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve monthly transaction summaries for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.get_transactions_by_month(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">categorize_a_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign a category to a transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.categorize_a_transaction(entity_id='entityId', transaction_id='transactionId', category_id='categoryId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity that owns the transaction
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — The ID of the transaction to categorize
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `str` — The ID of the category to assign
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">search_transactions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for transactions using various filters and text search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.search_transactions(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to search transactions for
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Text to search in transaction descriptions
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[PostV1TransactionsSearchRequestFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">chat_with_transactions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Interact with transactions using natural language
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.chat_with_transactions(entity_id='entityId', prompt='prompt', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity to chat about transactions for
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` — The natural language prompt
    
</dd>
</dl>

<dl>
<dd>

**history:** `typing.Optional[str]` — JSON string of conversation history
    
</dd>
</dl>

<dl>
<dd>

**context_data:** `typing.Optional[str]` — JSON string of additional context data
    
</dd>
</dl>

<dl>
<dd>

**custom_prompt:** `typing.Optional[str]` — Custom prompt to use instead of the main prompt
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[str]` — Whether to stream the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">get_entity_counterparties</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all counterparties for an entity with their transaction history and aggregated data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient
client = OpenLedgerClient(token="YOUR_TOKEN", )
client.transactions.get_entity_counterparties(entity_id='entityId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The ID of the entity
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of counterparties per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

