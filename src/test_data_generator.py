#!/usr/bin/env python3
"""
Test Data Generator - A utility for generating sample CSV data with configurable patterns.

This tool allows users to:
- Generate CSV files with custom schemas
- Support multiple data types (strings, numbers, dates)
- Create relationships between columns
- Include edge cases and random variations
"""

import random
import csv
import datetime
import string
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ColumnConfig:
    """Configuration for a single column in the test data."""
    name: str
    data_type: str  # 'string', 'integer', 'float', 'date', 'email', 'phone'
    min_value: Optional[Any] = None
    max_value: Optional[Any] = None
    pattern: Optional[str] = None
    related_to: Optional[str] = None  # Name of column this one relates to
    null_probability: float = 0.0  # Probability of generating NULL values

class TestDataGenerator:
    """Generates test data based on provided configuration."""
    
    def __init__(self, columns: List[ColumnConfig]):
        """Initialize the generator with column configurations."""
        self.columns = columns
        self.data: Dict[str, List[Any]] = {col.name: [] for col in columns}
    
    def _generate_string(self, config: ColumnConfig) -> str:
        """Generate a random string value."""
        if config.pattern:
            return config.pattern
        length = random.randint(5, 20)
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    def _generate_integer(self, config: ColumnConfig) -> int:
        """Generate a random integer value."""
        min_val = config.min_value if config.min_value is not None else 0
        max_val = config.max_value if config.max_value is not None else 1000
        return random.randint(min_val, max_val)
    
    def _generate_float(self, config: ColumnConfig) -> float:
        """Generate a random float value."""
        min_val = config.min_value if config.min_value is not None else 0.0
        max_val = config.max_value if config.max_value is not None else 1000.0
        return round(random.uniform(min_val, max_val), 2)
    
    def _generate_date(self, config: ColumnConfig) -> str:
        """Generate a random date value."""
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2023, 12, 31)
        days_between = (end_date - start_date).days
        random_days = random.randint(0, days_between)
        random_date = start_date + datetime.timedelta(days=random_days)
        return random_date.isoformat()
    
    def _generate_email(self, config: ColumnConfig) -> str:
        """Generate a random email address."""
        domains = ['example.com', 'test.org', 'sample.net']
        name_length = random.randint(5, 10)
        name = ''.join(random.choices(string.ascii_lowercase, k=name_length))
        domain = random.choice(domains)
        return f"{name}@{domain}"
    
    def _generate_phone(self, config: ColumnConfig) -> str:
        """Generate a random phone number."""
        area_code = random.randint(100, 999)
        prefix = random.randint(100, 999)
        line = random.randint(1000, 9999)
        return f"{area_code}-{prefix}-{line}"
    
    def _generate_value(self, config: ColumnConfig) -> Any:
        """Generate a value based on the column configuration."""
        if random.random() < config.null_probability:
            return None
            
        generators = {
            'string': self._generate_string,
            'integer': self._generate_integer,
            'float': self._generate_float,
            'date': self._generate_date,
            'email': self._generate_email,
            'phone': self._generate_phone
        }
        
        generator = generators.get(config.data_type)
        if not generator:
            raise ValueError(f"Unsupported data type: {config.data_type}")
            
        return generator(config)
    
    def generate_data(self, num_rows: int) -> None:
        """Generate the specified number of rows of test data."""
        for _ in range(num_rows):
            for column in self.columns:
                value = self._generate_value(column)
                self.data[column.name].append(value)
    
    def save_to_csv(self, filepath: str) -> None:
        """Save the generated data to a CSV file."""
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow([col.name for col in self.columns])
            # Write data rows
            for i in range(len(self.data[self.columns[0].name])):
                row = [self.data[col.name][i] for col in self.columns]
                writer.writerow(row)

def main():
    """Example usage of the TestDataGenerator."""
    # Example configuration
    columns = [
        ColumnConfig(name="id", data_type="integer", min_value=1, max_value=1000),
        ColumnConfig(name="name", data_type="string"),
        ColumnConfig(name="email", data_type="email"),
        ColumnConfig(name="registration_date", data_type="date"),
        ColumnConfig(name="score", data_type="float", min_value=0.0, max_value=100.0),
        ColumnConfig(name="phone", data_type="phone", null_probability=0.1)
    ]
    
    generator = TestDataGenerator(columns)
    generator.generate_data(num_rows=100)
    generator.save_to_csv("sample_data.csv")

if __name__ == "__main__":
    main()
