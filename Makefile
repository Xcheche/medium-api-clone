# ╔══════════════════════════════════════════════════════════════════╗
# ║           📚 Medium API Clone - Makefile Commands               ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🐳 Docker Commands:
#   make build          - Build and start Docker containers
#   make up             - Start Docker containers
#   make down           - Stop Docker containers
#   make down-v         - Stop containers and remove volumes
#   make show-logs      - Show logs for all services
#   make show-logs-api  - Show API logs only
#
# 🗄️  Database Commands:
#   make makemigrations - Create new database migrations
#   make migrate        - Apply database migrations
#   make authors-db     - Connect to PostgreSQL database
#   make volume         - Inspect postgres volume
#
# 👤 User Management:
#   make superuser      - Create Django superuser
#
# 📦 Static Files:
#   make collectstatic  - Collect static files
#
# 🎨 Code Quality:
#   make black          - Format code with black
#   make black-check    - Check code formatting
#   make black-diff     - Show formatting differences
#   make isort          - Sort imports with isort
#   make isort-check    - Check import sorting
#   make isort-diff     - Show import sorting differences
#   make flake8         - Run flake8 linter
#
# ═══════════════════════════════════════════════════════════════════

.PHONY: build up down show-logs show-logs-api makemigrations migrate
.PHONY: collectstatic superuser down-v volume authors-db flake8
.PHONY: black-check black-diff black isort-check isort-diff isort

#==================================================================
# Define the web service name for reuse
WEB_SERVICE_NAME = api


build:
	@echo "🏗️  Building Docker containers..."
	docker compose -f local.yml up --build -d --remove-orphans

config:
	@echo "🔧 Displaying docker-compose configuration..."
	docker compose -f local.yml config

up:
	@echo "🚀 Starting Docker containers..."
	docker compose -f local.yml up -d

down:
	@echo "🛑 Stopping Docker containers..."
	docker compose -f local.yml down

restart:
	@echo "🔄 Restarting Docker containers..."
	docker compose -f local.yml down
	docker compose -f local.yml up -d

show-logs:
	@echo "📋 Showing logs for all services..."
	docker compose -f local.yml logs

show-logs-api:
	@echo "📋 Showing API logs..."
	docker compose -f local.yml logs $(WEB_SERVICE_NAME)

check-migration:
	@echo "🗂️  checking before  migrations..."
	docker compose -f local.yml run --rm $(WEB_SERVICE_NAME) python manage.py makemigrations --check --dry-run


makemigrations:
	@echo "🗂️  Creating database migrations..."
	docker compose -f local.yml run --rm $(WEB_SERVICE_NAME) python manage.py makemigrations

migrate:
	@echo "🗂️  Applying database migrations..."
	docker compose -f local.yml run --rm $(WEB_SERVICE_NAME) python manage.py migrate

collectstatic:
	@echo "📦 Collecting static files..."
	docker compose -f local.yml run --rm $(WEB_SERVICE_NAME) python manage.py collectstatic --no-input --clear

superuser:
	@echo "👤 Creating superuser..."
	docker compose -f local.yml run --rm $(WEB_SERVICE_NAME) python manage.py createsuperuser

down-v:
	@echo "🗑️  Stopping containers and removing volumes..."
	docker compose -f local.yml down -v

volume:
	@echo "💾 Inspecting postgres volume..."
	docker volume inspect src_local_postgres_data

authors-db:
	@echo "🗄️  Connecting to database..."
	docker compose -f local.yml exec postgres psql --username=cheche --dbname=medium

flake8:
	@echo "🔍 Running flake8 linter..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) flake8 .

black-check:
	@echo "✅ Checking code formatting with black..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) black --check --exclude=migrations .

black-diff:
	@echo "📊 Showing black formatting diff..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) black --diff --exclude=migrations .

black:
	@echo "🎨 Formatting code with black..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) black --exclude=migrations .

isort-check:
	@echo "✅ Checking import sorting with isort..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) isort . --check-only --skip venv --skip migrations

isort-diff:
	@echo "📊 Showing isort diff..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) isort . --diff --skip venv --skip migrations

isort:
	@echo "🔤 Sorting imports with isort..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) isort . --skip venv --skip migrations


create-app:
	@echo "📦 Creating new Django app..."
	docker compose -f local.yml run --rm $(WEB_SERVICE_NAME) python manage.py startapp $(name)



shell:
	@echo "🖥️  Starting interactive shell..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) python manage.py shell

run-script:
	@if [ -z "$(runscript)" ]; then \
		echo "❌ Missing runscript. Use: make run-script runscript=users_scripts"; \
		exit 1; \
	fi
	@echo "📜 Running custom script..."
	docker compose -f local.yml exec $(WEB_SERVICE_NAME) python manage.py runscript $(runscript)	
	#usage: make run-script runscript=your_script_name (without .py extension)	

Verify-package:
	@echo "🔍 Verifying if django-phonenumber-field is installed..."
	docker compose -f local.yml run --rm api pip show django-phonenumber-field

