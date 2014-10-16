
=begin
checks our data for syntax errors and compliance with the schema
=end

require "kwalify"
require "yaml"

def validate(kind)
  validator = Kwalify::Validator.new(
                YAML.load_file(File.join("_tests", "schemas",
                                         "#{kind.chop}.yaml")))

  Dir[File.join(kind, "*.yaml")].each do |filename|
    errors = validator.validate(YAML.load_file(filename))
    if errors && !errors.empty?
      puts filename
      errors.each { |error| puts "\t[#{error.path}] #{error.message}" }
    end
  end
end

validate "bills"
validate "committee_reports"
validate "mps"
validate "plenary_sittings"
