import pandas as pd
import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):
    def __init__(self, num_features, hidden_channels, num_classes):
        super(GCN, self).__init__()
        torch.manual_seed(42)
        self.conv1 = GCNConv(num_features, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, num_classes)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

def load_data(csv_file='data/processed/processed_data.csv'):
    df = pd.read_csv(csv_file)
    companies = df['company'].unique()
    num_nodes = len(companies)
    company_to_idx = {company: idx for idx, company in enumerate(companies)}
    
    # Create node features using the 'value' column
    features = []
    for company in companies:
        value = df[df['company'] == company]['value'].mean()
        features.append([value])
    x = torch.tensor(features, dtype=torch.float)

    # Create edges between companies that share the same date
    edge_list = []
    grouped = df.groupby('date')['company'].apply(list)
    for date, comp_list in grouped.items():
        if len(comp_list) > 1:
            for i in range(len(comp_list)):
                for j in range(i+1, len(comp_list)):
                    src = company_to_idx[comp_list[i]]
                    dst = company_to_idx[comp_list[j]]
                    edge_list.append([src, dst])
                    edge_list.append([dst, src])
    if edge_list:
        edge_index = torch.tensor(edge_list, dtype=torch.long).t().contiguous()
    else:
        edge_index = torch.empty((2, 0), dtype=torch.long)
    
    # For demonstration, generate random labels (e.g., 2 classes)
    y = torch.randint(0, 2, (num_nodes,), dtype=torch.long)
    
    data = Data(x=x, edge_index=edge_index, y=y)
    return data, num_nodes, x.shape[1]

def train():
    data, num_nodes, num_features = load_data()
    model = GCN(num_features=num_features, hidden_channels=16, num_classes=2)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    
    model.train()
    for epoch in range(1, 101):
        optimizer.zero_grad()
        out = model(data)
        loss = F.nll_loss(out, data.y)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch:03d}, Loss: {loss:.4f}")
    print("Training completed.")

if __name__ == '__main__':
    train()
