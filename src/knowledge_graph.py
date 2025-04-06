from neo4j import GraphDatabase
import pandas as pd

class KnowledgeGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def create_company_node(self, tx, company, value, date):
        query = (
            "MERGE (c:Company {name: $company}) "
            "SET c.value = $value, c.date = $date"
        )
        tx.run(query, company=company, value=value, date=date)
    
    def create_relationship(self, tx, company1, company2):
        query = (
            "MATCH (a:Company {name: $company1}), (b:Company {name: $company2}) "
            "MERGE (a)-[:RELATED_TO]->(b)"
        )
        tx.run(query, company1=company1, company2=company2)
    
    def build_graph_from_csv(self, csv_file='data/processed/processed_data.csv'):
        df = pd.read_csv(csv_file)
        with self.driver.session() as session:
            # Create nodes for each company
            for _, row in df.iterrows():
                session.write_transaction(self.create_company_node, row['company'], row['value'], row['date'])
            
            # Create dummy relationships: relate companies that share the same date
            grouped = df.groupby('date')['company'].apply(list)
            for date, companies in grouped.items():
                if len(companies) > 1:
                    # Create pairwise relationships
                    for i in range(len(companies)):
                        for j in range(i+1, len(companies)):
                            session.write_transaction(self.create_relationship, companies[i], companies[j])
            print("Knowledge graph construction completed.")

def main():
    # Replace with your Neo4j connection details
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"
    
    kg = KnowledgeGraph(uri, user, password)
    kg.build_graph_from_csv()
    kg.close()

if __name__ == '__main__':
    main()
