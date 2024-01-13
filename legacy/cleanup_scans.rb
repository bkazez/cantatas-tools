#!/usr/bin/env ruby

# --debug to override

DEBUG = false.freeze
DEBUG_SAMPLE_SIZE = 3.freeze

# Source: Stack Overflow
def interleave(a, b)
  if a.length >= b.length
    a.zip(b)
  else
    b.zip(a).map(&:reverse)
  end.flatten.compact
end

SPLITTER_REGEX = /--/.freeze
BASENAME_REGEX = /^\d{4}-\d{2}-\d{2}[a-z]?\s+(.*)/i.freeze

contrast = ARGV[0]
if contrast.empty?
  puts "Please specify contrast as first arg."
  exit
end

# Parse optional args, which appear after the images
all_images = ARGV[1..]
nosplit = all_images.delete('--nosplit')
debug = DEBUG || all_images.delete('--debug')
rotation_angle = 180
all_images.each do |arg|
  if arg.start_with?('--rotate=')
    _, rotation_angle = arg.split('=')
    all_images.delete(arg)
  end
end

# Decide on an output filename
if File.basename(File.dirname(all_images.first)) =~ BASENAME_REGEX
  basename = "#{$1.strip}"
else
  basename = "scan"
end

if nosplit
  rectos, versos = all_images, nil
else
  rectos, versos = all_images.slice_after(SPLITTER_REGEX).to_a if !nosplit
end
rectos = rectos&.sample(DEBUG_SAMPLE_SIZE, random: Random.new(0)) if debug
versos = versos&.sample(DEBUG_SAMPLE_SIZE, random: Random.new(0)) if debug
sorted_images = interleave(rectos, versos || [])

args = []

args += %w[-orient Undefined] # remove EXIF orientation data that the camera sometimes erroneously adds
args += %w[-rotate] + [rotation_angle.to_s]
args += %w[-channel G -separate] # avoid chromatic aberration by taking just one channel
args += %w[-unsharp 3x3]
args += %W[-sigmoidal-contrast #{contrast}]
args += %w[-level 1%,97%]

# split dual-page scan vertically: https://legacy.imagemagick.org/Usage/crop/#crop_equal
args += %w[-crop 2x1@ +repage] if versos.nil? && !nosplit

#args += %W[-define pdf:producer=magick\ #{args.join(' ')}] # put settings in metadata if desired

outfile = "../scores/#{basename}.pdf"
args << outfile

puts "rectos=#{rectos&.count} versos=#{versos&.count}"
puts "magick=#{sorted_images.map { |s| "\"#{s}\"" }.join(' ')} #{args.map { |s| "\"#{s}\"" }.join(' ')}"

system('magick', *sorted_images, *args)
system('open', outfile) if debug