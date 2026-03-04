"""
Online Voting System
Console-based voting system with admin panel and voter features
Data stored in .txt files using simple file operations
"""

import os
import hashlib
from datetime import datetime

# File paths for data storage
ADMIN_FILE = "admin.txt"
VOTERS_FILE = "voters.txt"
CANDIDATES_FILE = "candidates.txt"
VOTES_FILE = "votes.txt"

class VotingSystem:
    def __init__(self):
        self.initialize_files()
        self.current_user = None
        self.user_type = None
        
    def initialize_files(self):
        """Initialize data files if they don't exist"""
        # Create admin file with default admin (username: admin, password: admin123)
        if not os.path.exists(ADMIN_FILE):
            with open(ADMIN_FILE, 'w') as f:
                # Format: username|hashed_password
                admin_pass = self.hash_password("admin123")
                f.write(f"admin|{admin_pass}\n")
        
        # Create empty files for voters, candidates, and votes
        for file in [VOTERS_FILE, CANDIDATES_FILE, VOTES_FILE]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    pass
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # ==================== AUTHENTICATION ====================
    
    def admin_login(self):
        """Admin login functionality"""
        print("\n" + "="*50)
        print("ADMIN LOGIN")
        print("="*50)
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        hashed_password = self.hash_password(password)
        
        with open(ADMIN_FILE, 'r') as f:
            for line in f:
                stored_username, stored_password = line.strip().split('|')
                if username == stored_username and hashed_password == stored_password:
                    self.current_user = username
                    self.user_type = "admin"
                    print("\n✓ Admin login successful!")
                    input("Press Enter to continue...")
                    return True
        
        print("\n✗ Invalid admin credentials!")
        input("Press Enter to continue...")
        return False
    
    def voter_registration(self):
        """Register a new voter"""
        print("\n" + "="*50)
        print("VOTER REGISTRATION")
        print("="*50)
        
        voter_id = input("Enter Voter ID: ").strip()
        
        # Check if voter ID already exists
        if self.check_voter_exists(voter_id):
            print("\n✗ Voter ID already registered!")
            input("Press Enter to continue...")
            return False
        
        name = input("Enter Full Name: ").strip()
        password = input("Enter Password: ").strip()
        confirm_password = input("Confirm Password: ").strip()
        
        if password != confirm_password:
            print("\n✗ Passwords do not match!")
            input("Press Enter to continue...")
            return False
        
        hashed_password = self.hash_password(password)
        
        # Format: voter_id|name|hashed_password|has_voted(0=no, 1=yes)
        with open(VOTERS_FILE, 'a') as f:
            f.write(f"{voter_id}|{name}|{hashed_password}|0\n")
        
        print(f"\n✓ Registration successful! Your Voter ID: {voter_id}")
        input("Press Enter to continue...")
        return True
    
    def voter_login(self):
        """Voter login functionality"""
        print("\n" + "="*50)
        print("VOTER LOGIN")
        print("="*50)
        
        voter_id = input("Voter ID: ").strip()
        password = input("Password: ").strip()
        
        hashed_password = self.hash_password(password)
        
        voters = self.read_voters()
        
        for voter in voters:
            if voter['voter_id'] == voter_id and voter['password'] == hashed_password:
                self.current_user = voter_id
                self.user_type = "voter"
                print(f"\n✓ Welcome, {voter['name']}!")
                input("Press Enter to continue...")
                return True
        
        print("\n✗ Invalid voter credentials!")
        input("Press Enter to continue...")
        return False
    
    # ==================== DATA READING ====================
    
    def check_voter_exists(self, voter_id):
        """Check if voter ID already exists"""
        if not os.path.exists(VOTERS_FILE):
            return False
        
        with open(VOTERS_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    stored_id = line.split('|')[0]
                    if stored_id == voter_id:
                        return True
        return False
    
    def read_voters(self):
        """Read all voters from file"""
        voters = []
        if os.path.exists(VOTERS_FILE):
            with open(VOTERS_FILE, 'r') as f:
                for line in f:
                    if line.strip():
                        voter_id, name, password, has_voted = line.strip().split('|')
                        voters.append({
                            'voter_id': voter_id,
                            'name': name,
                            'password': password,
                            'has_voted': has_voted
                        })
        return voters
    
    def read_candidates(self):
        """Read all candidates from file"""
        candidates = []
        if os.path.exists(CANDIDATES_FILE):
            with open(CANDIDATES_FILE, 'r') as f:
                for line in f:
                    if line.strip():
                        candidate_id, name, symbol = line.strip().split('|')
                        candidates.append({
                            'candidate_id': candidate_id,
                            'name': name,
                            'symbol': symbol
                        })
        return candidates
    
    def read_votes(self):
        """Read all votes from file"""
        votes = []
        if os.path.exists(VOTES_FILE):
            with open(VOTES_FILE, 'r') as f:
                for line in f:
                    if line.strip():
                        voter_id, candidate_id, timestamp = line.strip().split('|')
                        votes.append({
                            'voter_id': voter_id,
                            'candidate_id': candidate_id,
                            'timestamp': timestamp
                        })
        return votes
    
    # ==================== ADMIN FUNCTIONS ====================
    
    def add_candidate(self):
        """Add a new candidate (Admin only)"""
        print("\n" + "="*50)
        print("ADD CANDIDATE")
        print("="*50)
        
        candidate_id = input("Enter Candidate ID: ").strip()
        
        # Check if candidate ID already exists
        candidates = self.read_candidates()
        for candidate in candidates:
            if candidate['candidate_id'] == candidate_id:
                print("\n✗ Candidate ID already exists!")
                input("Press Enter to continue...")
                return False
        
        name = input("Enter Candidate Name: ").strip()
        symbol = input("Enter Candidate Symbol: ").strip()
        
        # Format: candidate_id|name|symbol
        with open(CANDIDATES_FILE, 'a') as f:
            f.write(f"{candidate_id}|{name}|{symbol}\n")
        
        print(f"\n✓ Candidate '{name}' added successfully!")
        input("Press Enter to continue...")
        return True
    
    def view_all_voters(self):
        """View all registered voters (Admin only)"""
        print("\n" + "="*50)
        print("ALL REGISTERED VOTERS")
        print("="*50)
        
        voters = self.read_voters()
        
        if not voters:
            print("\nNo voters registered yet.")
        else:
            print(f"\nTotal Voters: {len(voters)}\n")
            print(f"{'Voter ID':<15} {'Name':<25} {'Voted':<10}")
            print("-" * 50)
            for voter in voters:
                voted_status = "Yes" if voter['has_voted'] == '1' else "No"
                print(f"{voter['voter_id']:<15} {voter['name']:<25} {voted_status:<10}")
        
        input("\nPress Enter to continue...")
    
    def view_results(self):
        """View voting results (Admin only)"""
        print("\n" + "="*50)
        print("VOTING RESULTS")
        print("="*50)
        
        candidates = self.read_candidates()
        votes = self.read_votes()
        
        if not candidates:
            print("\nNo candidates available.")
            input("\nPress Enter to continue...")
            return
        
        # Count votes for each candidate
        vote_count = {}
        for candidate in candidates:
            vote_count[candidate['candidate_id']] = 0
        
        for vote in votes:
            if vote['candidate_id'] in vote_count:
                vote_count[vote['candidate_id']] += 1
        
        # Display results
        print(f"\nTotal Votes Cast: {len(votes)}\n")
        print(f"{'Candidate ID':<15} {'Name':<25} {'Symbol':<15} {'Votes':<10}")
        print("-" * 65)
        
        # Sort by votes (descending)
        sorted_candidates = sorted(candidates, 
                                   key=lambda x: vote_count[x['candidate_id']], 
                                   reverse=True)
        
        for candidate in sorted_candidates:
            c_id = candidate['candidate_id']
            print(f"{c_id:<15} {candidate['name']:<25} {candidate['symbol']:<15} {vote_count[c_id]:<10}")
        
        # Declare winner
        if votes:
            winner = sorted_candidates[0]
            winner_votes = vote_count[winner['candidate_id']]
            print("\n" + "="*65)
            print(f"🏆 WINNER: {winner['name']} ({winner['symbol']}) with {winner_votes} votes!")
            print("="*65)
        
        input("\nPress Enter to continue...")
    
    def admin_panel(self):
        """Admin dashboard"""
        while True:
            self.clear_screen()
            print("\n" + "="*50)
            print("ADMIN PANEL")
            print("="*50)
            print(f"Logged in as: {self.current_user}")
            print("-" * 50)
            print("1. Add Candidate")
            print("2. View All Candidates")
            print("3. View All Voters")
            print("4. View Voting Results")
            print("5. Logout")
            print("="*50)
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.add_candidate()
            elif choice == '2':
                self.view_candidates()
            elif choice == '3':
                self.view_all_voters()
            elif choice == '4':
                self.view_results()
            elif choice == '5':
                self.current_user = None
                self.user_type = None
                print("\n✓ Logged out successfully!")
                input("Press Enter to continue...")
                break
            else:
                print("\n✗ Invalid choice!")
                input("Press Enter to continue...")
    
    # ==================== VOTER FUNCTIONS ====================
    
    def view_candidates(self):
        """View all candidates"""
        print("\n" + "="*50)
        print("CANDIDATES LIST")
        print("="*50)
        
        candidates = self.read_candidates()
        
        if not candidates:
            print("\nNo candidates available yet.")
        else:
            print(f"\n{'Candidate ID':<15} {'Name':<25} {'Symbol':<15}")
            print("-" * 55)
            for candidate in candidates:
                print(f"{candidate['candidate_id']:<15} {candidate['name']:<25} {candidate['symbol']:<15}")
        
        input("\nPress Enter to continue...")
    
    def has_voter_voted(self, voter_id):
        """Check if voter has already voted"""
        voters = self.read_voters()
        for voter in voters:
            if voter['voter_id'] == voter_id:
                return voter['has_voted'] == '1'
        return False
    
    def cast_vote(self):
        """Cast vote (Voter only)"""
        print("\n" + "="*50)
        print("CAST YOUR VOTE")
        print("="*50)
        
        # Check if already voted
        if self.has_voter_voted(self.current_user):
            print("\n✗ You have already voted! Multiple voting is not allowed.")
            input("Press Enter to continue...")
            return False
        
        # Display candidates
        candidates = self.read_candidates()
        
        if not candidates:
            print("\nNo candidates available for voting.")
            input("Press Enter to continue...")
            return False
        
        print("\nAvailable Candidates:\n")
        print(f"{'Candidate ID':<15} {'Name':<25} {'Symbol':<15}")
        print("-" * 55)
        for candidate in candidates:
            print(f"{candidate['candidate_id']:<15} {candidate['name']:<25} {candidate['symbol']:<15}")
        
        print("\n")
        candidate_id = input("Enter Candidate ID to vote for: ").strip()
        
        # Verify candidate exists
        candidate_exists = False
        for candidate in candidates:
            if candidate['candidate_id'] == candidate_id:
                candidate_exists = True
                selected_candidate = candidate
                break
        
        if not candidate_exists:
            print("\n✗ Invalid Candidate ID!")
            input("Press Enter to continue...")
            return False
        
        # Confirm vote
        print(f"\nYou are voting for: {selected_candidate['name']} ({selected_candidate['symbol']})")
        confirm = input("Confirm vote? (yes/no): ").strip().lower()
        
        if confirm != 'yes':
            print("\n✗ Vote cancelled.")
            input("Press Enter to continue...")
            return False
        
        # Record vote
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(VOTES_FILE, 'a') as f:
            f.write(f"{self.current_user}|{candidate_id}|{timestamp}\n")
        
        # Update voter status
        self.update_voter_status(self.current_user)
        
        print("\n✓ Vote cast successfully! Thank you for voting.")
        input("Press Enter to continue...")
        return True
    
    def update_voter_status(self, voter_id):
        """Mark voter as having voted"""
        voters = self.read_voters()
        
        with open(VOTERS_FILE, 'w') as f:
            for voter in voters:
                if voter['voter_id'] == voter_id:
                    voter['has_voted'] = '1'
                f.write(f"{voter['voter_id']}|{voter['name']}|{voter['password']}|{voter['has_voted']}\n")
    
    def voter_panel(self):
        """Voter dashboard"""
        while True:
            self.clear_screen()
            print("\n" + "="*50)
            print("VOTER PANEL")
            print("="*50)
            print(f"Logged in as: {self.current_user}")
            
            # Check voting status
            has_voted = self.has_voter_voted(self.current_user)
            status = "✓ VOTED" if has_voted else "✗ NOT VOTED"
            print(f"Voting Status: {status}")
            print("-" * 50)
            print("1. View Candidates")
            print("2. Cast Vote")
            print("3. Logout")
            print("="*50)
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                self.view_candidates()
            elif choice == '2':
                self.cast_vote()
            elif choice == '3':
                self.current_user = None
                self.user_type = None
                print("\n✓ Logged out successfully!")
                input("Press Enter to continue...")
                break
            else:
                print("\n✗ Invalid choice!")
                input("Press Enter to continue...")
    
    # ==================== MAIN MENU ====================
    
    def main_menu(self):
        """Main menu of the voting system"""
        while True:
            self.clear_screen()
            print("\n" + "="*50)
            print("     ONLINE VOTING SYSTEM")
            print("="*50)
            print("\n1. Admin Login")
            print("2. Voter Registration")
            print("3. Voter Login")
            print("4. Exit")
            print("="*50)
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                if self.admin_login():
                    self.admin_panel()
            elif choice == '2':
                self.voter_registration()
            elif choice == '3':
                if self.voter_login():
                    self.voter_panel()
            elif choice == '4':
                print("\n" + "="*50)
                print("Thank you for using Online Voting System!")
                print("="*50)
                break
            else:
                print("\n✗ Invalid choice!")
                input("Press Enter to continue...")

# ==================== RUN APPLICATION ====================

if __name__ == "__main__":
    system = VotingSystem()
    system.main_menu()
