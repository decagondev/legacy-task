from flask import Flask, request, jsonifyimport sqlite3
app = Flask(__name__)
def get_db_connection():
    return sqlite3.connect('support.db')

@app.route('/tickets/search', methods=['GET'])def search_tickets():
    query = request.args.get('q', '')

    conn = get_db_connection()
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM tickets WHERE title LIKE '%{query}%' OR description LIKE '%{query}%'"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            "id": row[0], "user_id": row[1], "title": row[2],
            "description": row[3], "category": row[4], "created_at": row[5]
        })
    return jsonify(results)

@app.route('/tickets/triage', methods=['POST'])def triage_ticket():
    data = request.get_json()
    ticket_id = data.get('id')
    manual_category = data.get('category')

    if ticket_id is not None:
        if manual_category in ['Billing', 'Technical', 'Account']:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tickets SET category = ? WHERE id = ?", (manual_category, ticket_id))
            conn.commit()
            conn.close()
            return jsonify({"status": "success", "message": "Category updated"})
        else:
            if not manual_category:
                return jsonify({"error": "Missing category"}), 400
            else:
                return jsonify({"error": "Invalid target category"}), 400
    else:
        return jsonify({"error": "Missing ticket ID"}), 400

@app.route('/tickets/extract', methods=['POST'])def extract_metadata():
    data = request.get_json()
    description = data.get('description', '')

    email = "unknown"
    if "email is" in description:
        parts = description.split("email is ")
        if len(parts) > 1:
            email = parts[1].split(" ")[0]

    return jsonify({
        "extracted_email": email,
        "raw_input": description
    })
if __name__ == '__main__':
    app.run(port=5000)
