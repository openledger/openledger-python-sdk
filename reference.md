# Reference
## Transactions
<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">get_transactions_by_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.get_transactions_by_company(
    id="id",
)

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

**id:** `str` — Company ID
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.create_a_new_transaction(
    id_="id",
)

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

**id_:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier for the transaction
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.datetime]` — Date of the transaction
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — Amount of the transaction
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency of the transaction
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the transaction
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TransactionStatus]` — Status of the transaction
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[int]` — ID of the user who created the transaction
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[int]` — ID of the user who last updated the transaction
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — Date when the transaction was created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — Date when the transaction was last updated
    
</dd>
</dl>

<dl>
<dd>

**bank_transaction_id:** `typing.Optional[str]` — ID of the bank transaction
    
</dd>
</dl>

<dl>
<dd>

**transaction_type:** `typing.Optional[TransactionTransactionType]` — Type of transaction
    
</dd>
</dl>

<dl>
<dd>

**ledger_type:** `typing.Optional[TransactionLedgerType]` — Ledger type of the transaction
    
</dd>
</dl>

<dl>
<dd>

**bank_account_id:** `typing.Optional[str]` — ID of the bank account
    
</dd>
</dl>

<dl>
<dd>

**business_id:** `typing.Optional[str]` — ID of the business
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[TransactionDirection]` — Direction of the transaction
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — Balance after the transaction
    
</dd>
</dl>

<dl>
<dd>

**counterparty_name:** `typing.Optional[str]` — Name of the counterparty
    
</dd>
</dl>

<dl>
<dd>

**categorization_status:** `typing.Optional[TransactionCategorizationStatus]` — Status of categorization
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[int]` — ID of the category
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — ID of the company
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional metadata for the transaction
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.edit_a_transaction(
    id_="id",
    transaction_id="transactionId",
)

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

**id_:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — Transaction ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier for the transaction
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.datetime]` — Date of the transaction
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — Amount of the transaction
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency of the transaction
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the transaction
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TransactionStatus]` — Status of the transaction
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[int]` — ID of the user who created the transaction
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[int]` — ID of the user who last updated the transaction
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — Date when the transaction was created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — Date when the transaction was last updated
    
</dd>
</dl>

<dl>
<dd>

**bank_transaction_id:** `typing.Optional[str]` — ID of the bank transaction
    
</dd>
</dl>

<dl>
<dd>

**transaction_type:** `typing.Optional[TransactionTransactionType]` — Type of transaction
    
</dd>
</dl>

<dl>
<dd>

**ledger_type:** `typing.Optional[TransactionLedgerType]` — Ledger type of the transaction
    
</dd>
</dl>

<dl>
<dd>

**bank_account_id:** `typing.Optional[str]` — ID of the bank account
    
</dd>
</dl>

<dl>
<dd>

**business_id:** `typing.Optional[str]` — ID of the business
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[TransactionDirection]` — Direction of the transaction
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — Balance after the transaction
    
</dd>
</dl>

<dl>
<dd>

**counterparty_name:** `typing.Optional[str]` — Name of the counterparty
    
</dd>
</dl>

<dl>
<dd>

**categorization_status:** `typing.Optional[TransactionCategorizationStatus]` — Status of categorization
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[int]` — ID of the category
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — ID of the company
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional metadata for the transaction
    
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

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">export_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.export_transaction(
    id="id",
)

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

**id:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ExportTransactionRequestFormat]` — Export format
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date for filtering transactions
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date for filtering transactions
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.get_transactions_by_month(
    id="id",
    month="month",
)

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

**id:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**month:** `str` — Month in YYYY-MM format
    
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

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">prompt_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.prompt_transaction(
    id="id",
)

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

**id:** `str` — Company ID
    
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

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">classify_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.classify_transaction(
    id="id",
)

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

**id:** `str` — Company ID
    
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

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">generate_general_ledger</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.generate_general_ledger(
    id="id",
)

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

**id:** `str` — Company ID
    
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

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">bulk_create_transactions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient, Transaction

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.bulk_create_transactions(
    id="id",
    request=[Transaction()],
)

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

**id:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[Transaction]` 
    
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

<details><summary><code>client.transactions.<a href="src/openledger/transactions/client.py">suggest_transaction_categories</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.transactions.suggest_transaction_categories(
    id="id",
)

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

**id:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**transactions:** `typing.Optional[typing.Sequence[Transaction]]` 
    
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

## Companies
<details><summary><code>client.companies.<a href="src/openledger/companies/client.py">create_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.companies.create_company()

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

**legal_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tin:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**us_state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**developer_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.companies.<a href="src/openledger/companies/client.py">get_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.companies.get_company(
    id="id",
)

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

**id:** `str` — Company ID
    
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

<details><summary><code>client.companies.<a href="src/openledger/companies/client.py">update_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.companies.update_company(
    id="id",
    request={"key": "value"},
)

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

**id:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
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

<details><summary><code>client.companies.<a href="src/openledger/companies/client.py">delete_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.companies.delete_company(
    id="id",
)

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

**id:** `str` — Company ID
    
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
<details><summary><code>client.categories.<a href="src/openledger/categories/client.py">get_categories_by_company</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.categories.get_categories_by_company(
    id="id",
)

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

**id:** `str` — Company ID
    
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

<details><summary><code>client.categories.<a href="src/openledger/categories/client.py">create_category</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from openledger import OpenLedgerClient

client = OpenLedgerClient(
    token="YOUR_TOKEN",
)
client.categories.create_category(
    id="id",
)

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

**id:** `str` — Company ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

